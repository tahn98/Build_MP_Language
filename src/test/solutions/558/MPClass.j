.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i F from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label3
Label2:
	iconst_1
	istore_2
Label4:
	iload_2
	bipush 10
	if_icmplt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	iload_2
	invokestatic io/putInt(I)V
Label5:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label4
Label6:
Label3:
	ldc 10.5
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
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
