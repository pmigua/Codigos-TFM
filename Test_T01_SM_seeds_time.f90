program Test_T01_SM_seeds_time
  implicit none

  integer :: iyear, iday, ihour, imin, isec
  integer :: i, j, k, nlat, nlon, nr, npoints, ios
  real :: vgsex, vgsey, vgsez
  real :: psi, pi, deg2rad
  real :: rseed, lat_deg, lon_deg, lat_rad, lon_rad
  real :: xsm, ysm, zsm, xgsw, ygsw, zgsw
  character(len=256) :: filename, arg

  common /GEOPACK1/ A(12),DS3,BB(2),PSI_COMMON,CC(18)
  real :: A, DS3, BB, PSI_COMMON, CC

  ! Usage:
  !   Test_T01_SM_seeds_time.exe seeds_000.vtk 1997 90 21 0 0
  !
  ! The seed points are defined in SM spherical coordinates at magnetic
  ! latitudes |lambda_SM| >= 60 deg, then transformed to GSW coordinates,
  ! because the Tsyganenko/IGRF field VTK is written in GSW coordinates.

  call get_command_argument(1, filename)
  if (len_trim(filename) == 0) filename = 'T01_SM_seeds_000.vtk'

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

  pi = 3.14159265358979323846
  deg2rad = pi/180.0

  ! Solar wind velocity required by RECALC_08.
  vgsex = -400.0
  vgsey = 0.0
  vgsez = 0.0

  call RECALC_08(iyear, iday, ihour, imin, isec, vgsex, vgsey, vgsez)
  psi = PSI_COMMON

  ! Seed distribution.
  ! nr     : number of radial shells in SM coordinates.
  ! nlat   : latitudes per hemisphere: 60, 65, 70, 75, 80, 85 deg.
  ! nlon   : longitudes: 0, 15, 30, ..., 345 deg.
  nr = 1
  nlat = 6
  nlon = 24
  npoints = 2 * nr * nlat * nlon

  open(unit=10, file=trim(filename), status='replace', action='write')

  write(10,'(A)') '# vtk DataFile Version 3.0'
  write(10,'(A)') 'SM polar seed points transformed to GSW coordinates'
  write(10,'(A)') 'ASCII'
  write(10,'(A)') 'DATASET POLYDATA'
  write(10,'(A,I8,A)') 'POINTS ', npoints, ' float'

  do k = 1, nr
     rseed = 1.5   ! Re. Increase/add shells if more coverage is needed.

     ! Northern hemisphere: +60 to +85 deg SM latitude.
     do i = 1, nlat
        lat_deg = 60.0 + 5.0*real(i-1)
        lat_rad = lat_deg*deg2rad
        do j = 1, nlon
           lon_deg = 15.0*real(j-1)
           lon_rad = lon_deg*deg2rad
           xsm = rseed*cos(lat_rad)*cos(lon_rad)
           ysm = rseed*cos(lat_rad)*sin(lon_rad)
           zsm = rseed*sin(lat_rad)
           call SMGSW_08(xsm, ysm, zsm, xgsw, ygsw, zgsw, 1)
           write(10,'(3F15.6)') xgsw, ygsw, zgsw
        end do
     end do

     ! Southern hemisphere: -60 to -85 deg SM latitude.
     do i = 1, nlat
        lat_deg = -60.0 - 5.0*real(i-1)
        lat_rad = lat_deg*deg2rad
        do j = 1, nlon
           lon_deg = 15.0*real(j-1)
           lon_rad = lon_deg*deg2rad
           xsm = rseed*cos(lat_rad)*cos(lon_rad)
           ysm = rseed*cos(lat_rad)*sin(lon_rad)
           zsm = rseed*sin(lat_rad)
           call SMGSW_08(xsm, ysm, zsm, xgsw, ygsw, zgsw, 1)
           write(10,'(3F15.6)') xgsw, ygsw, zgsw
        end do
     end do
  end do

  write(10,'(A,I8,I8)') 'VERTICES ', npoints, 2*npoints
  do i = 0, npoints-1
     write(10,'(I2,1X,I8)') 1, i
  end do

  write(10,'(A,I8)') 'POINT_DATA ', npoints
  write(10,'(A)') 'SCALARS hemisphere int 1'
  write(10,'(A)') 'LOOKUP_TABLE default'

  do i = 1, nr*nlat*nlon
     write(10,'(I2)') 1
  end do
  do i = 1, nr*nlat*nlon
     write(10,'(I2)') -1
  end do

  close(10)

  write(*,'(A)') 'Generated seed file: '//trim(filename)
  write(*,'(A,F10.4,A)') 'PSI = ', psi*180.0/pi, ' deg'
end program Test_T01_SM_seeds_time
