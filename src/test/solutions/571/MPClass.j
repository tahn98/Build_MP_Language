.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static printhello()Ljava/lang/String;
Label0:
	ldc "hello"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is str1 Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/printhello()Ljava/lang/String;
	astore_1
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
