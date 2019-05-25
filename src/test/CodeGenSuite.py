import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    '''
    def test01(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test02(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(1); end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test03(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(1.2); end"""
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test04(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(143.15e5); end"""
        expect = "1.4315E7"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test05(self):
        input = """
        procedure main();
        var a : integer; 
        begin
            a:=2;
            putInt(a);      
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test06(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=b:=2;
            putInt(b);
            putInt(a);
        end
        """
        expect = "22"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test07(self):
        input = """
        procedure main();
        var a : real;
        begin
            a:= 2.2;
            putFloat(a);
        end
        """
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test08(self):
        input = """
        procedure main();
        var a : real; b:real;
        begin
            a := b := 2.2;
            putFloat(a);
            putFloat(b);
        end
        """
        expect = "2.22.2"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test09(self):
        input = """
        procedure main();
        var a : real; b:real;
        begin
            a := b := 2;
            putFloat(a);
            putFloat(b);
        end
        """
        expect = "2.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test10(self):
        input = """
        procedure main();
        var a : real; b:real;
        begin
            b := a := b := 2;
            putFloat(a);
            putFloat(b);
        end
        """
        expect = "2.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test10(self):
        input = """
        procedure main();
        var a : real; b:real; 
        begin
            b := a := b := 2;
            putFloat(a);
            putFloat(b);
        end
        """
        expect = "2.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test11(self):
        input = """
        procedure main();
        var a : real; b:real; c:real;
        begin
            b := a := b := 2;
            putFloat(b);
            c := a;
            b := 3;
            putFloat(b);
        end
        """
        expect = "2.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test12(self):
        input = """
        procedure main();
        var a : real; b:real; c:real;
        begin
            a:=1;
            b:=2;
            c:=3;
            a:=b+c;
            putFloat(a);
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test13(self):
        input = """
        procedure main();
        var a : real; b:integer; c:real;
        begin
            a:=1;
            b:=2;
            c:=3;
            a:=b+c;
            putFloat(a);
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test14(self):
        input = """
        procedure main();
        var a : real; b:integer; c:real;
        begin
            a:=1;
            b:=2;
            c:=3;
            a:=b*c;
            putFloat(a);
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test15(self):
        input = """
        procedure main();
        var a : real; b:integer; c:real;
        begin
            a:=1;
            b:=2;
            c:=3;
            a:=b*c*2;
            putFloat(a);
        end
        """
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test16(self):
        input = """
        procedure main();
        var a : integer;b:integer;
        begin
            b := 2;
            a := b*2+40;
            putInt(a);
        end
        """
        expect = "44"
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test17(self):
        input = """
        procedure main();
        var a,b,c,d : integer;
        begin
            a:=2;
            b:=2;
            c:=2;
            d:=2;
            d := a*b-c;
            putInt(d);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test18(self):
        input = """
        procedure main();
        var a,b,c,d : integer;
        begin
            a:=2;
            b:=2;
            c:=2;
            d:=2;
            putInt(2+2+2+2);
        end
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test19(self):
        input = """
        procedure main();
        var a,b,c,d : integer;
        begin
            a:=2;
            b:=2;
            c:=2;
            d:=2;
            putInt(a+a+a+a);
        end
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test20(self):
        input = """
        procedure main();
        var a,b,c,d : integer;
        begin
            a:=2;
            b:=a+a-a;
            putInt(b);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test21(self):
        input = """
        procedure main();
        var a,b,c,d : integer;
        begin
            a:=b:=c:=10;
            d:=a+b-c*a-a;
            putInt(d);
        end
        """
        expect = "-90"
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    def test22(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a:= 6 div 2;
            putInt(a);
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test23(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=1;
            b:=2;
            putInt(a > b);
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test24(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=3;
            b:=2;
            putInt(a > b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test25(self):
        input = """
        procedure main();
        var a,b,c : real;
        begin
            a:=3.0;
            b:=2;
            putInt(a > b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test26(self):
        input = """
        procedure main();
        var a,b,c : real;
        begin
            a:=3.0;
            b:=2;
            putInt(a <= b);
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test27(self):
        input = """
        procedure main();
        var a,b,c : real;
        begin
            a:=3.0;
            b:=2;
            putInt(a < b);
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    def test28(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=3;
            putInt(a <> b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test29(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=3;
            putInt(a <> b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test30(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=2;
            putInt(a = b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    

    def test31(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=2;
            putInt(a = b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test32(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=1;
            b:=2;
            if (b > a) then
                b:=3;            
            putInt(b);
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test33(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=1;
            b:=2;
            if (b > a) then
                b:=3; 
            else
                b:=1;           
            putInt(b);
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test34(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=1;
            if (b > a) then
                b:=3; 
            else
                b:=1;           
            putInt(b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    def test35(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=2;
            if (b = a) then
                b:=100; 
            else
                b:=1;           
            putInt(b);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test36(self):
        input = """
        procedure main();
        var a,b,c : integer;
        begin
            a:=2;
            b:=2;
            if (a = b) then
                b:=100; 
            else
                b:=1;           
            putInt(b);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test37(self):
        input = """
        procedure main();
        var a,b,c : real;
        begin
            a:=2;
            b:=2;
            if (a = b) then
                b:=100; 
            else
                b:=1;           
            putFloat(b);
        end
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test38(self):
        input = """
        procedure main();
        var a : real; b:integer;
        begin
            a:=2;
            b:=2;
            putInt(a=b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test39(self):
        input = """
        procedure main();
        var a : real; b:integer;
        begin
            a:=2;
            b:=3;
            putInt(a<>b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test40(self):
        input = """
        var a : real;
        procedure main();
        var b : real; 
        begin
            a:=2;
            b:=3;
            putInt(a<>b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test41(self):
        input = """
        var a : real;
        procedure main();
        var b : real; 
        begin
            a := 1;
            b := 2;
            if (a = 1) then
                if (b=2) then
                    b := 100;
                else
                    b := 10;

            putFloat(b);
        end
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    def test42(self):
        input = """
        var a : real;
        procedure main();
        var b : real; 
        begin
            a := 1;
            b := 2;
            if (a = 10) then
                if (b=2) then
                    b := 100;
                else
                    b := 10;
            else
                b:=50;

            putFloat(b);
        end
        """
        expect = "50.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test43(self):
        input = """
        procedure main();
        var a,b : integer;
        begin   
            a:=1;
            b:=5;
            while (a>b) do
                a:=a+1;
            putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test44(self):
        input = """
        procedure main();
        var a,i : integer;
        begin   
            a:=0;
            for i:=1 to 5 do
                a:=a+1;

            putInt(a);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test45(self):
        input = """
        procedure main();
        var i:integer;
        begin   
            i:=0;
            i:=i+1;
            putInt(i);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test46(self):
        input = """
        procedure main();
        var i:integer;
        begin   
            i:=3;
            putInt(i>=3);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test47(self):
        input = """
        procedure main();
        var a,b:integer;
        begin
            a:=1;  
            b:=5; 
            while (a<b) do
                a:=a+1;
            putInt(a);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test48(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            while (i<5) do
                begin
                    a:=a+1;
                    i:=i+1;
                end
            putInt(a);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test49(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            while (i<=5) do
                begin
                    a:=a+1;
                    i:=i+1;
                end
            putInt(a);
        end
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test50(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            while (i<=5) do
                begin
                    a:=a+1;
                    i:=i+1;
                end
            putInt(a);
        end
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test51(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            for i:=1 to 10 do
                putInt(i);
        end
        """
        expect = "12345678910"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test52(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            for i:=10 downto 1 do
                putInt(i);
        end
        """
        expect = "10987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test53(self):
        input = """
        procedure main();
        var a,i : integer;
        begin
            a:=0;
            i:=0;
            for i:=10 downto 1 do
                putInt(i);
        end
        """
        expect = "10987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test54(self):
        input = """
        var a : real;
        procedure main();
        var a : integer;
        begin
            a:=2;
            putInt(2);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test55(self):
        input = """
        var a : real; 
        procedure main();
        var b : integer;
        begin
            a:=2;
            b:=3;
            putFloat(a+b);
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test56(self):
        input = """
        var a : real; 
        procedure main();
        var b : integer;
        begin
            with m:integer; do
                begin
                m:=1;
                putInt(m);
                end
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test57(self):
        input = """
        procedure main();
        begin
            with i:integer; do
                for i:=1 to 10 do
                    putInt(i);
        end
        """
        expect = "12345678910"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test58(self):
        input = """
        procedure main();
        var i:real;
        begin
            with i:integer; do
                for i:=1 to 10 do
                    putInt(i);

            i:=10.5;
            putFloat(i);
        end
        """
        expect = "1234567891010.5"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test59(self):
        input = """
        function a(x:integer; y:integer):integer;
        begin
            return 1;
        end
        procedure main();
        var i:integer;x,y:integer;
        begin
            x:=1;
            y:=2;
            i:=a(x,y);
            putInt(i);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test60(self):
        input = """
        function a():real;
        begin
            return 1;
        end
        procedure main();
        var i:real;
        begin
            i:=a();
            putFloat(i);
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test61(self):
        input = """
        procedure main();
        var i:real;
        begin
            putFloat(3/2);
        end
        """
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test62(self):
        input = """
        procedure main();
        var i:real;
        begin
            putInt(3 div 2);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test63(self):
        input = """
        procedure main();
        var i:real;
        begin
            putInt(3 mod 2);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test64(self):
        input = """
        procedure main();
        var i:real;
        begin
            putInt(4 mod 2);
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test65(self):
        input = """
        function print(a:real; b:real):real;
        begin
            return a+b;
        end
        procedure main();
        var a,b : real; sum:real;
        begin
            a:=b:=1;
            sum:=print(a,b);
            putFloat(sum);
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test66(self):
        input = """
        function print(a:real; b:real):real;
        begin
            return a+b;
        end
        procedure main();
        var sum:real;
        begin
            sum:=print(1,1.0);
            putFloat(sum);
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test67(self):
        input = """
        procedure main();
        begin
            putBool(1>2);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test68(self):
        input = """
        function a():boolean;
        begin
            return true;
        end
        procedure main();
        var b : boolean;
        begin
            b := a();
            putBool(b);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test69(self):
        input = """
        procedure main();
        var str1 : string;
        begin
            putString("meomeo");
        end
        """
        expect = "meomeo"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test70(self):
        input = """
        function printhello():string;
        begin
            return "hello";
        end
        procedure main();
        var str1 : string;
        begin
            str1 := printhello();
            putString(str1);
        end
        """
        expect = "hello"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test71(self):
        input = """
        function printhello():string;
        begin
            return "hello";
        end
        procedure main();
        var str1 : string;
        begin
            str1 := printhello();
            putString(str1);
        end
        """
        expect = "hello"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test72(self):
        input = """
        function printhello(a : string):string;
        begin
            return "hello";
        end
        procedure main();
        var str1 : string;
        begin
            str1 := printhello("hello");
            putString(str1);
        end
        """
        expect = "hello"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test73(self):
        input = """
        procedure main();
        var a:integer;
        begin
            putInt(1);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test74(self):
        input = """
        procedure main();
        begin
            putBool(true);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    def test75(self):
        input = """
        procedure main();
        begin
            putInt(-1);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    

    def test_76(self):
        input = """
            function tong(a,b:integer):integer;
            begin
                return a+b;
            end
            function square(x:integer):integer;
            begin
                return x*x;
            end
            function sub(x,y:integer):integer;
            begin
                return x-y;
            end
            procedure main ();
            begin
                putInt(square(sub(1,2)*tong(1,2)));
            end
            """ 
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    
    def test_77(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (x > 100) then
                putStringLn("100 < x < 200");
            else if (x > 200) then
                putStringLn("200 < x < 300");
            else if (x > 300) then
                putStringLn("x > 300");
            else 
            begin
                if (x > 100) then
                 x := x + 100;
            end
            putIntLn(x);
        end
"""
        expect = """100 < x < 200
123
"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))
    
    def test_78(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("askdjadklj");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (x > 100) then
                putStringLn("100 < x < 200");
            else if (x > 200) then
                putStringLn("200 < x < 300");
            else if (x > 300) then
                putStringLn("x > 300");
            else 
            begin
                if (x > 100) then
                 x := x + 100;
            end
            putIntLn(x);
        end
"""
        expect = """100 < x < 200
123
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    def test_79(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (true and false) then
                x := x - 100;
            putIntLn(x);
        end
        """
        expect = """123\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_80(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (false and false) then
                x := x - 100;
            putIntLn(x);
        end
        """
        expect = """123\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_81(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 1+2;
            if (false and false) then
                x := x - 100;
            putIntLn(x);
        end
        """
        expect = """3\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test82(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 1;
            while x <= 10 do
            begin
 putIntLn(x);
                if x = 10 then putStringLn("lmao");

                x := x + 1;
            end
        end
        """
        expect = """1
2
3
4
5
6
7
8
9
10
lmao
"""
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_83(self):
        input = """
        var i:integer;
        procedure main();
        begin
            i := 1;
            with i:integer; do
            begin
                i := 2;
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_84(self):
        input = """
        procedure main();
        begin
            if true then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    def test_86(self):
        input = """
        procedure main();
        begin
            if false then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_87(self):
        input = """
		procedure main();
		begin
			putIntLn(1+2);
            putIntLn(1-2);
            putIntLn(1*2);
            putIntLn(1 div 2);
            putIntLn(31 mod 4);
            putFloatLn(1/2);
            putBoolLn(1 > 2);
            putBoolLn(1 < 2);
            putBoolLn(1 <= 2);
			return;
		end
		"""
        expect = "3\n-1\n2\n0\n3\n0.5\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_88(self):
        input = """
		procedure main();
		begin
            // same result as AND
			putBoolLn(true and then false);
            putBoolLn(true and then true);
            putBoolLn(false and then true);
            putBoolLn(false and then false);
            // skip evaluation of the second operand --> no error
            putBoolLn(false and then 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_85(self):
        input = """
        function sumofdigit(n:integer):integer;
        begin
            if(n<10) then return n;
            else return (n mod 10) + sumofdigit(n div 10);
        end
        procedure main ();
        begin
            putInt(sumofdigit(1234));
        end
        """ 
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_89(self):
        input = """
        function temp(n:integer):boolean;
        begin
            if(n=5) then return true;
            else return false;
        end
        procedure main ();
        begin
            putBool(temp(5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_90(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)or(2>1));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    def test_91(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)and(2>1));
        end
        """ 
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_92(self):
        input = """
        procedure main ();
        begin
            putBool(((1>2)or(2>1))and(100<1000));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_93(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)or(1>1)or(3<15.5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_94(self):
        input = """
        procedure main ();
        begin
            putBool((1<2)or else(1>1)or else(3<15.5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test95(self):
        input = """
function isPrime(x: integer): boolean;
var i : integer;
begin
    for i := 2 to x div 2 do
    begin
        if x mod i = 0 then return false;
    end

    return true;
end

procedure main();
var x, i : integer;
begin
    i := 0;
    x := 100;

    while i <= x do
    begin
        if isPrime(i) then putIntLn(i);
        i := i + 1;
    end

end
        """
        expect = """0
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""
        self.assertTrue(TestCodeGen.test(input, expect, 595))
        
    def test96(self):
        input = """
function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end

procedure main();
var s, i : integer;
begin
    i := 1;
    s := 0;

    while i <= 10 do 
    begin
        putIntLn(fact(i));
        i := i + 1;
    end

end
        """
        expect = """1
2
6
24
120
720
5040
40320
362880
3628800
"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))     

    def test97(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;

    while i <= 10 do 
    begin
        if (i > 4) and (i < 7) then 
        begin
            i := i + 1;
            continue;
        end

        s := 0;
        for j := i * 10 to (i + 1)*10 do
        begin
            if (j mod 2 = 0) then continue;
            s := s + j;
        end
        putInt(i);
        putString(", ");
        putInt(s);
        putLn();
        i := i + 1;
    end

end

function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end
        """
        expect = """1, 75
2, 125
3, 175
4, 225
7, 375
8, 425
9, 475
10, 525
"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))   

    def test98(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        var x: real;
        begin 
            X:=10;
            putfloat(X);
            with
                x,y:boolean;
            do begin
                with 
                    x:integer;
                do begin
                    x:=1;
                    putInt(x);
                end
            end
        end"""
        expect = "10.01"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test99(self):
        """Simple program: int main() {} """
        input = """
        function sum(a,n:integer):integer;
        begin
            if n<0 then return 0;
            else return n + sum(a,n-1);
        end
        procedure main();
        var a,b:integer;
        begin
            a:=1;
            b:=9;
            PUTINT(sum(a,b));
        end
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,599))
    def test100(self):
        """Simple program: int main() {} """
        input = """
        function digit1(n:integer):integer;
        begin
            if n<10 then return n;
            return digit1(n div 10);
        end
        procedure main();
        var a,b:integer;
        begin
            PUTINT(digit1(14526));
            PUTINT(digit1(4526));
        end
        """
        expect = "14"
        self.assertTrue(TestCodeGen.test(input,expect,600))
'''
    def testx(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i:=1 to 5 do
            begin
                putInt(1);
                i:=i+1;
            end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 601))
   

    



    





    

    
    
