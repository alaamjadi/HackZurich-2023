instanceKlass com/android/dx/rop/annotation/AnnotationsList
instanceKlass com/android/dx/rop/cst/CstArray$List
instanceKlass com/android/dx/cf/attrib/InnerClassList
TEST configureArchitecture from PETSc.options.arch(/sandbox/petsc/petsc.next/config/PETSc/options/arch.py:43)
XDG_SESSION_ID=9192
_=/sandbox/petsc/petsc.next/lib/petsc/bin/maint/buildtest
SSH_CONNECTION=140.221.8.249 35558 140.221.11.38 22
OLDPWD=/home/petsc
PWD=/sandbox/petsc/petsc.next
MAIL=/var/mail/petsc
MACHTYPE=x86_64
================================================================================
TEST resetEnvCompilers from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1609)
TESTING: resetEnvCompilers from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1609)
================================================================================
TEST checkEnvCompilers from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1639)
TESTING: checkEnvCompilers from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1639)
================================================================================
TEST checkMPICompilerOverride from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1572)
TESTING: checkMPICompilerOverride from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1572)
  Check if --with-mpi-dir is used along with CC CXX or FC compiler options.
    This usually prevents mpi compilers from being used - so issue a warning
================================================================================
TEST requireMpiLdPath from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1593)
TESTING: requireMpiLdPath from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:1593)
  OpenMPI wrappers require LD_LIBRARY_PATH set
================================================================================
TEST checkInitialFlags from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:446)
TESTING: checkInitialFlags from config.setCompilers(/sandbox/petsc/petsc.next/config/BuildSystem/config/setCompilers.py:446)
  Initialize the compiler and linker flags
          Initialized CFLAGS to 
          Initialized CFLAGS to 
          Initialized LDFLAGS to 
tdf#97035 FILEOPEN: RTF wrong cell width [Mike Kaganski]
tdf#97228 Split up include files in include/vcl where possible into separate public and internal parts [Shubham Verma]
Checking for program /sbin/nvcc...not found
Checking for program /bin/nvcc...not found
Checking for program /usr/games/nvcc...not found
Checking for program /usr/local/games/nvcc...not found
Checking for program /sandbox/petsc/petsc.next/lib/petsc/bin/win32fe/nvcc...not found
Checking for program /Developer/NVIDIA/CUDA-6.5/bin/nvcc...not found
Checking for program /sandbox/petsc/petsc.next/lib/petsc/bin/win32fe/nvcc...not found
Checking for program /usr/local/cuda/bin/nvcc...found
              Defined make macro "CUDAC" to "/usr/local/cuda/bin/nvcc"
Executing: /usr/local/cuda/bin/nvcc -c -o /tmp/petsc-uGvYRc/config.setCompilers/conftest.o -I/tmp/petsc-uGvYRc/config.setCompilers  -Wno-deprecated-gpu-targets /tmp/petsc-uGvYRc/config.setCompilers/conftest.cu 
Successful compile:
Source:
#include "confdefs.h"
#include "conffix.h"

int main() {
;
Successful compile:
Source:
#include "confdefs.h"
#include "conffix.h"

int main() {
;
  return 0;
}
Executing: mpicxx  -o /tmp/petsc-uGvYRc/config.setCompilers/conftest    /tmp/petsc-uGvYRc/config.setCompilers/conftest.o  -lpetsc-ufod4vtr9mqHvKIQiVAm
Possible ERROR while running linker: exit code 1
stderr:
/usr/bin/ld: cannot find -lpetsc-ufod4vtr9mqHvKIQiVAm
      2          1           0        0.000000    0.000000    0.957200
      3          1           0        0.926627    0.000000   -0.239987
  <MemoFn>Loading memos from /u/nlp/rte/natlog/memos/lex/tagSim.memos.ser.gz...</MemoFn>
 Framework group  C2V[C2(O),SGV(H2)]
 Deg. of freedom     2
 Full point group                 C2V     NOp   4
 Largest Abelian subgroup         C2V     NOp   4
 Largest concise Abelian subgroup C2      NOp   2
PROC_CREATOR_COUNT Be9 : alphaInelastic = 1
instanceKlass sun/misc/Launcher$AppClassLoader$1
instanceKlass sun/misc/URLClassPath
instanceKlass java/security/Principal
instanceKlass java/security/ProtectionDomain$Key
instanceKlass java/security/ProtectionDomain$2
instanceKlass sun/misc/JavaSecurityProtectionDomainAccess
instanceKlass java/security/ProtectionDomain$JavaSecurityAccessImpl
instanceKlass sun/misc/JavaSecurityAccess
instanceKlass java/net/URLStreamHandler
instanceKlass java/net/Parts
instanceKlass java/util/BitSet
instanceKlass sun/net/www/ParseUtil
instanceKlass java/io/FileInputStream$1
instanceKlass java/lang/CharacterData
instanceKlass sun/util/locale/LocaleUtils
instanceKlass java/util/Locale$LocaleKey
instanceKlass sun/util/locale/BaseLocale$Key
instanceKlass sun/util/locale/BaseLocale
instanceKlass java/util/concurrent/ConcurrentHashMap$CollectionView
instanceKlass java/util/concurrent/ConcurrentHashMap$CounterCell
instanceKlass java/util/concurrent/ConcurrentHashMap$Node
instanceKlass java/util/concurrent/locks/ReentrantLock
instanceKlass java/util/concurrent/locks/Lock
instanceKlass java/util/concurrent/ConcurrentMap
instanceKlass sun/util/locale/LocaleObjectCache
instanceKlass java/util/Locale
instanceKlass java/lang/reflect/Array
instanceKlass java/io/Reader
instanceKlass sun/misc/MetaIndex
instanceKlass sun/misc/Launcher$ExtClassLoader$1
