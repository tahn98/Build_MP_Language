.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static a(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is x I from Label0 to Label1
.var 3 is y I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_2
	istore_3
	iload_2
	iload_3
	invokestatic MPClass/a(II)I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
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
