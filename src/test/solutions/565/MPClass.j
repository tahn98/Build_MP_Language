.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static print(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is sum F from Label0 to Label1
Label0:
	iconst_1
	i2f
	fstore_2
	fload_2
	fstore_1
	fload_1
	fload_2
	invokestatic MPClass/print(FF)F
	fstore_3
	fload_3
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 4
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
