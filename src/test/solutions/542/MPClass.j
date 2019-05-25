.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	iconst_1
	i2f
	putstatic MPClass.a F
	iconst_2
	i2f
	fstore_1
	getstatic MPClass.a F
	bipush 10
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_1
	iconst_2
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	bipush 100
	i2f
	fstore_1
	goto Label9
Label8:
	bipush 10
	i2f
	fstore_1
Label9:
	goto Label5
Label4:
	bipush 50
	i2f
	fstore_1
Label5:
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
