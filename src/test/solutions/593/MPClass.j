.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_1
	iconst_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	iconst_3
	i2f
	ldc 15.5
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
.limit locals 1
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
