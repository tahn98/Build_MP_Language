.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static a()Z
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	invokestatic MPClass/a()Z
	istore_1
	iload_1
	invokestatic io/putBool(Z)V
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
