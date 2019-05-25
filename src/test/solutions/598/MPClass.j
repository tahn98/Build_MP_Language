.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
	bipush 10
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
.var 2 is x Z from Label2 to Label3
.var 3 is y Z from Label2 to Label3
Label2:
.var 4 is x I from Label4 to Label5
Label4:
	iconst_1
	istore 4
	iload 4
	invokestatic io/putInt(I)V
Label5:
Label3:
Label1:
	return
.limit stack 1
.limit locals 5
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
