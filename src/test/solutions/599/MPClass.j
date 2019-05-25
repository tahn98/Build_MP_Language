.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static sum(II)I
.var 0 is a I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
	goto Label5
Label4:
	iload_1
	iload_0
	iload_1
	iconst_1
	isub
	invokestatic MPClass/sum(II)I
	iadd
	ireturn
Label5:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	bipush 9
	istore_2
	iload_1
	iload_2
	invokestatic MPClass/sum(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
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
