      PROGRAM Test_T01_cartesian

      EXTERNAL IGRF_GSW_08, T01_01

      REAL XG,YG,ZG
      REAL BX,BY,BZ,HX,HY,HZ,PDYN,PS,DST,BYIMF,BZIMF
      INTEGER RGRID,TGRID,PGRID,IOPT,RRR
      CHARACTER FILENAME*40
      DIMENSION PARMOD(10)
      
      
      COMMON /GEOPACK1/ A(12),DS3,BB(2),PSI,CC(18)
      COMMON /GEOPACK2/ G(105),H(105),REC(105)

      xmin=-50
      xmax=15
      ymin=-20
      ymax=20
      zmin=-20
      zmax=20

      nx=(xmax-xmin)+1
      ny=(ymax-ymin)+1
      nz=(zmax-zmin)+1
      
      XG=0.
      YG=0.
      ZG=0.
      
      PS=0.
      
      PDYN=3.
      DST=-20.
      BYIMF=-3.
      BZIMF=5.
      PARMOD(1)=PDYN
      PARMOD(2)=DST
      PARMOD(3)=BYIMF
      PARMOD(4)=BZIMF

      IOPT=1
      
      IYEAR=1997
      IDAY=90
      IHOUR=21
      IMIN=0
      ISEC=0

      VGSEX=-400.0
      VGSEY=0.
      VGSEZ=0.
      CALL RECALC_08 (IYEAR,IDAY,IHOUR,IMIN,ISEC,VGSEX,VGSEY,VGSEZ)
      


      WRITE(FILENAME,'(''Test_T01_cartesian.vtk'')')
      OPEN(UNIT=1,FILE=FILENAME)

      WRITE (1,'(''# vtk DataFile Version 3.0'')')
      WRITE (1,'(''vtk output'')')
      WRITE (1,'(''ASCII'')')
      WRITE (1,'(''DATASET STRUCTURED_GRID'')')
      WRITE (1,'(''DIMENSIONS '',3I5)') nx,ny,nz
      WRITE (1,'(''POINTS '',I7,'' float'')') nx*ny*nz

      DO 10 ZG=zmin, zmax
        DO 10 YG=ymin, ymax
            DO 10 XG=xmin, xmax
c               CALL SPHCAR_08 (RE,THETA,PHI,XG,YG,ZG,1)
                WRITE (1,'(3F15.3)') XG,YG,ZG
                WRITE (*,'(3F15.3)') XG,YG,ZG
10    CONTINUE

      WRITE (1,'(''POINT_DATA '',I7)') nx*ny*nz
      WRITE (1,'(''VECTORS igrf float'')')
      
      DO 20 ZG=zmin, zmax
        DO 20 YG=ymin, ymax
            DO 20 XG=xmin, xmax
c              CALL SPHCAR_08 (RE,THETA,PHI,XG,YG,ZG,1)
               CALL T01_01 (IOPT,PARMOD,PS,XG,YG,ZG,BX,BY,BZ)
               CALL IGRF_GSW_08 (XG,YG,ZG,HX,HY,HZ)
               HX=HX+BX
               HY=HY+BY
               HZ=HZ+BZ
               WRITE (1,'(3F15.2)') HX,HY,HZ
               WRITE (*,'(3F15.2)') HX,HY,HZ
20    CONTINUE


      END
