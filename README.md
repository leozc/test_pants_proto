# test_pants_proto

## to trigger the error

```bash
pants check src/jvm::  


07:43:08.45 [INFO] Starting new nailgun server with cmd: "/bin/bash", args ["__jdk/jdk.sh", "__java_home/bin/java", "-cp", "__jdk/com.martiansoftware_nailgun-server_0.9.1.jar:__toolcp/com.fasterxml.jackson.core_jackson-annotations_2.12.4.jar:__toolcp/com.fasterxml.jackson.core_jackson-core_2.12.4.jar:__toolcp/com.fasterxml.jackson.core_jackson-databind_2.12.4.jar:__toolcp/com.fasterxml.jackson.datatype_jackson-datatype-jdk8_2.12.4.jar:__toolcp/com.github.javaparser_javaparser-core_3.25.5.jar:__toolcp/com.github.javaparser_javaparser-symbol-solver-core_3.25.5.jar:__toolcp/com.google.code.findbugs_jsr305_3.0.2.jar:__toolcp/com.google.errorprone_error_prone_annotations_2.18.0.jar:__toolcp/com.google.guava_failureaccess_1.0.1.jar:__toolcp/com.google.guava_guava_32.1.2-jre.jar:__toolcp/com.google.guava_listenablefuture_9999.0-empty-to-avoid-conflict-with-guava.jar:__toolcp/com.google.j2objc_j2objc-annotations_2.8.jar:__toolcp/org.checkerframework_checker-qual_3.33.0.jar:__toolcp/org.javassist_javassist_3.29.2-GA.jar:__processorcp", "-Xmx512m", "com.martiansoftware.nailgun.NGServer", ":0"], in cwd /private/var/folders/b8/g3hm3b6s1js3qq6j315gsp8c0000gn/T/pants-sandbox-BR5iqv
07:43:09.21 [ERROR] 1 Exception encountered:

Engine traceback:
  in `check` goal

ClasspathSourceMissing: No JVM classpath providers (from: CompileJavaSourceRequest, CoursierFetchRequest, DeployJarClasspathEntryRequest, JvmResourcesRequest) were compatible with the combination of inputs:
  * 3rdparty/python:delta-spark#protobuf	(python_requirement)
```