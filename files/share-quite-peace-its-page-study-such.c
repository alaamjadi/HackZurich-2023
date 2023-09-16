Successful compile:
Source:
#include "confdefs.h"
#include "conffix.h"

int main() {
;
  return 0;
}
Executing: /usr/local/cuda/bin/nvcc  -o /tmp/petsc-uGvYRc/config.setCompilers/conftest   -Xcompiler -fPIC /tmp/petsc-uGvYRc/config.setCompilers/conftest.o 
            Valid CUDA linker flag -Wl,-rpath,/sandbox/petsc/petsc.next
================================================================================
TEST checkLibC from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1415)
TESTING: checkLibC from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1415)
  Test whether we need to explicitly include libc in shared linking
       - Mac OSX requires an explicit reference to libc for shared linking
Executing: mpicc -c -o /tmp/petsc-uGvYRc/config.setCompilers/conftest.o -I/tmp/petsc-uGvYRc/config.setCompilers   /tmp/petsc-uGvYRc/config.setCompilers/conftest.c 
Successful compile:
Source:
#include "confdefs.h"
#include "conffix.h"
#include <stdlib.h> 
int foo(void) {void *chunk = malloc(31); free(chunk); return 0;}
Executing: mpicc  -o /tmp/petsc-uGvYRc/config.setCompilers/libconftest.so  -shared  /tmp/petsc-uGvYRc/config.setCompilers/conftest.o 
          Shared linking does not require an explicit libc reference
================================================================================
TEST checkDynamicLinker from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1464)
TESTING: checkDynamicLinker from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1464)
  Check that the linker can dynamicaly load shared libraries
Checking for header: dlfcn.h
Importing categories...
0 K2 categories imported
0 categories imported
build	14-Jul-2020 09:19:57	[DEBUG] === PROJECT BUILD PLAN ================================================
build	14-Jul-2020 09:19:57	[DEBUG] Project:       com.XXXXXX.eps.epdg:epdg-app-aggregator:1.0.16-SNAPSHOT
build	14-Jul-2020 09:19:57	[DEBUG] Dependencies (collect): []
build	14-Jul-2020 09:19:57	[DEBUG] Dependencies (resolve): [test]
build	14-Jul-2020 09:19:57	[DEBUG] Repositories (dependencies): [Artifactory (https://artifactory.XXXXXX.com/artifactory/public/, default, releases)]
 NAtoms=    3 NActive=    3 NUniq=    2 SFac= 1.69D+00 NAtFMM=   80 NAOKFM=F Big=F
 One-electron integrals computed using PRISM.
 NBasis=    19 RedAO= T  NBF=    10     1     3     5
 NBsUse=    19 1.00D-06 NBFU=    10     1     3     5
 Harris functional with IExCor=  205 diagonalized for initial guess.
 ExpMin= 1.61D-01 ExpMax= 5.48D+03 ExpMxC= 8.25D+02 IAcc=1 IRadAn=         1 AccDes= 0.00D+00
 HarFok:  IExCor=  205 AccDes= 0.00D+00 IRadAn=         1 IDoV= 1
 ScaDFX=  1.000000  1.000000  1.000000  1.000000
 FoFCou: FMM=F IPFlag=           0 FMFlag=      100000 FMFlg1=           0
         NFxFlg=           0 DoJE=T BraDBF=F KetDBF=T FulRan=T
         Omega=  0.000000  0.000000  1.000000  0.000000  0.000000 ICntrl=     500 IOpCl=  0
         NMat0=    1 NMatS0=    1 NMatT0=    0 NMatD0=    1 NMtDS0=    0 NMtDT0=    0
         I1Cent=           4 NGrid=           0.
 Petite list used in FoFCou.
 Initial guess orbital symmetries:
       Occupied  (A1) (A1) (B2) (A1) (B1)
       Virtual   (A1) (B2) (B2) (A1) (B1) (A1) (B2) (A1) (A1) (A2)
                 (B1) (A1) (B2) (A1)
 The electronic state of the initial guess is 1-A1.
 Requested convergence on RMS density matrix=1.00D-08 within 128 cycles.
 Requested convergence on MAX density matrix=1.00D-06.
 Requested convergence on             energy=1.00D-06.
 No special actions if energy rises.
 Keep R1 ints in memory in canonical form, NReq=857956.
 ZZZY=              0.0000 XXYY=             -2.0407 XXZZ=             -1.9288 YYZZ=             -1.5867
 XXYZ=              0.0000 YYXZ=              0.0000 ZZXY=              0.0000
 N-N= 9.194964814020D+00 E-N=-1.988764411604D+02  KE= 7.582152800362D+01
 Symmetry A1   KE= 6.774138068715D+01
 Symmetry A2   KE= 6.005298651141D-35
 Symmetry B1   KE= 4.554718000640D+00
	at info.magnolia.cms.filters.MgnlFilterChain.doFilter(MgnlFilterChain.java:79) [magnolia-core-6.2.3.jar:?]
	at info.magnolia.cms.filters.MgnlFilterChain.doFilter(MgnlFilterChain.java:81) [magnolia-core-6.2.3.jar:?]
	at info.magnolia.cms.security.auth.login.LoginFilter.doFilter(LoginFilter.java:127) [magnolia-core-6.2.3.jar:?]
<images/datadriven/SI_Directness.png, id=1824, 1057.41335pt x 933.7284pt>
File: images/datadriven/SI_Directness.png Graphic file (type png)
ofz#4982 integer-overflow [Caolán McNamara]
ofz#4983 divide-by-zero [Caolán McNamara]
ofz#4990 direct-leak [Caolán McNamara]
Running ModalFeaturizer
build	14-Jul-2020 09:19:57	[DEBUG]   Imported: org.apache.maven.project < plexus.core
[  1%] Completed 'G4NEUTRONXS'
     Event                    : 

[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.WarnIfTimeLimitExceeded:0]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.TimeLimitExceededMultiplier:1.5]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.TimeLimitExceededMinTime:0.005]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.UseBackgroundLevelStreaming:1]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.UnregisterComponentsTimeLimit:1.0]]
[2023.05.20-22.07.39:930][  0]LogConfig: Set CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[s.MaxPackageSummarySize:16384]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: Set CVar [[s.FlushStreamingOnExit:1]]
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[FixedBootOrder:/Script/Engine/Default__SoundBase]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[FixedBootOrder:/Script/Engine/Default__MaterialInterface]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[FixedBootOrder:/Script/Engine/Default__DeviceProfileManager]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.GarbageCollectionSettings] File [Engine]
[2023.05.20-22.07.39:931][  0]LogConfig: Set CVar [[gc.MaxObjectsNotConsideredByGC:1]]
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.SelectiveBasePassOutputs]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.DBuffer]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.Symbols]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.GenerateSymbols]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.WriteSymbols]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.AllowUniqueSymbols]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.ExtraData]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.Shaders.Optimize]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.CompileShadersForDevelopment]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.MobileHDR]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[VersionedIntRValues:r.UsePreExposure]] deferred - dummy variable created
[2023.05.20-22.07.39:931][  0]LogConfig: CVar [[bCookOnTheFlyForLaunchOn:1]] deferred - dummy variable created
[2023.05.20-22.07.39:932][  0]LogConsoleManager: Warning: Setting the console variable 'r.ScreenPercentage' with 'SetByScalability' was ignored as it is lower priority than the previous 'SetByProjectSetting'. Value remains '100'
