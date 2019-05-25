.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is c F from Label0 to Label1
Label0:
	iconst_2
	i2f
	fstore_1
	iconst_2
	i2f
	fstore_2
	fload_1
	fload_2
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	bipush 100
	i2f
	fstore_2
	goto Label5
Label4:
	iconst_1
	i2f
	fstore_2
Label5:
	fload_2
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
