program Test_T01_cartesian_time_v2
  implicit none

  external IGRF_GSW_08, T01_01

  integer :: iyear, iday, ihour, imin, isec, ios
  integer :: nx, ny, nz
  real :: xmin, xmax, ymin, ymax, zmin, zmax
  real :: xg, yg, zg
  real :: bx, by, bz, hx, hy, hz
  real :: pdyn, ps, dst, byimf, bzimf
  real :: vgsex, vgsey, vgsez
  real :: r2
  integer :: iopt
  real :: parmod(10)
  character(len=256) :: filename, arg

  common /GEOPACK1/ A(12),DS3,BB(2),PSI,CC(18)
  common /GEOPACK2/ G(105),H(105),REC(105)
  real :: A, DS3, BB, PSI, CC, G, H, REC

  ! Usage:
  !   Test_T01_cartesian_time_v2.exe field_000.vtk 1997 90 21 0 0

  call get_command_argument(1, filename)
  if (len_trim(filename) == 0) filename = 'T01_field_000.vtk'

  call get_command_argument(2, arg); read(arg, *, iostat=ios) iyear
  if (ios /= 0) iyear = 1997
  call get_command_argument(3, arg); read(arg, *, iostat=ios) iday
  if (ios /= 0) iday = 90
  call get_command_argument(4, arg); read(arg, *, iostat=ios) ihour
  if (ios /= 0) ihour = 21
  call get_command_argument(5, arg); read(arg, *, iostat=ios) imin
  if (ios /= 0) imin = 0
  call get_command_argument(6, arg); read(arg, *, iostat=ios) isec
  if (ios /= 0) isec = 0

  xmin = -50.0
  xmax =  10.0
  ymin = -10.0
  ymax =  10.0
  zmin = -10.0
  zmax =  10.0

  nx = int(xmax - xmin) + 1
  ny = int(ymax - ymin) + 1
  nz = int(zmax - zmin) + 1

  pdyn = 3.0
  dst = -20.0
  byimf = -3.0
  bzimf = 5.0

  parmod = 0.0
  parmod(1) = pdyn
  parmod(2) = dst
  parmod(3) = byimf
  parmod(4) = bzimf

  iopt = 1

  vgsex = -400.0
  vgsey = 0.0
  vgsez = 0.0
  call RECALC_08(iyear, iday, ihour, imin, isec, vgsex, vgsey, vgsez)
  ps = PSI

  open(unit=1, file=trim(filename), status='replace', action='write')

  write(1,'(A)') '# vtk DataFile Version 3.0'
  write(1,'(A)') 'T01 + IGRF magnetic field in GSW coordinates'
  write(1,'(A)') 'ASCII'
  write(1,'(A)') 'DATASET STRUCTURED_GRID'
  write(1,'(A,3I6)') 'DIMENSIONS ', nx, ny, nz
  write(1,'(A,I8,A)') 'POINTS ', nx*ny*nz, ' float'

  do zg = zmin, zmax
     do yg = ymin, ymax
        do xg = xmin, xmax
           write(1,'(3F15.6)') xg, yg, zg
        end do
     end do
  end do

  write(1,'(A,I8)') 'POINT_DATA ', nx*ny*nz
  write(1,'(A)') 'VECTORS B_total float'

  do zg = zmin, zmax
     do yg = ymin, ymax
        do xg = xmin, xmax
           r2 = xg*xg + yg*yg + zg*zg
           if (r2 < 1.0) then
              hx = 0.0
              hy = 0.0
              hz = 0.0
           else
              call T01_01(iopt, parmod, ps, xg, yg, zg, bx, by, bz)
              call IGRF_GSW_08(xg, yg, zg, hx, hy, hz)
              hx = hx + bx
              hy = hy + by
              hz = hz + bz
           end if
           write(1,'(3ES16.7)') hx, hy, hz
        end do
     end do
  end do

  close(1)

  write(*,'(A)') 'Generated field file: '//trim(filename)
  write(*,'(A,F10.4,A)') 'PSI = ', ps*180.0/3.14159265358979323846, ' deg'
end program Test_T01_cartesian_time_v2
