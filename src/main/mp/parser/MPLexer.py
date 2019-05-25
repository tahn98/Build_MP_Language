# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0254\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3")
        buf.write("K\3L\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3P\3P\3Q\3Q\3Q\3Q\7")
        buf.write("Q\u01ce\nQ\fQ\16Q\u01d1\13Q\3Q\3Q\3Q\3Q\3Q\3R\3R\7R\u01da")
        buf.write("\nR\fR\16R\u01dd\13R\3R\3R\3R\3R\3S\3S\3S\3S\7S\u01e7")
        buf.write("\nS\fS\16S\u01ea\13S\3S\3S\3T\6T\u01ef\nT\rT\16T\u01f0")
        buf.write("\3T\3T\3U\3U\7U\u01f7\nU\fU\16U\u01fa\13U\3V\3V\3V\7V")
        buf.write("\u01ff\nV\fV\16V\u0202\13V\3V\3V\3V\3W\3W\3W\3X\6X\u020b")
        buf.write("\nX\rX\16X\u020c\3Y\6Y\u0210\nY\rY\16Y\u0211\3Y\3Y\6Y")
        buf.write("\u0216\nY\rY\16Y\u0217\3Y\5Y\u021b\nY\5Y\u021d\nY\3Y\5")
        buf.write("Y\u0220\nY\3Y\3Y\3Y\5Y\u0225\nY\3Y\3Y\3Y\5Y\u022a\nY\5")
        buf.write("Y\u022c\nY\3Z\3Z\5Z\u0230\nZ\3Z\6Z\u0233\nZ\rZ\16Z\u0234")
        buf.write("\3[\3[\3[\3\\\3\\\3\\\3\\\7\\\u023e\n\\\f\\\16\\\u0241")
        buf.write("\13\\\3\\\3\\\3]\3]\3]\3]\5]\u0249\n]\7]\u024b\n]\f]\16")
        buf.write("]\u024e\13]\3]\3]\3]\3]\3]\4\u01cf\u01db\2^\3\3\5\2\7")
        buf.write("\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35")
        buf.write("\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29")
        buf.write("\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23")
        buf.write("Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m\36o\37q s!u")
        buf.write("\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b")
        buf.write("-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097\63\u0099")
        buf.write("\64\u009b\65\u009d\66\u009f\67\u00a18\u00a39\u00a5:\u00a7")
        buf.write(";\u00a9<\u00ab=\u00ad\2\u00af>\u00b1?\u00b3\2\u00b5@\u00b7")
        buf.write("A\u00b9B\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg")
        buf.write("\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2N")
        buf.write("Nnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4")
        buf.write("\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{")
        buf.write("{\4\2\\\\||\5\2\n\f\16\17\"\"\4\2\f\f\17\17\3\2\"\"\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^\n\2$$))^^d")
        buf.write("dhhppttvv\4\2--//\2\u024e\2\3\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\3\u00bb")
        buf.write("\3\2\2\2\5\u00be\3\2\2\2\7\u00c0\3\2\2\2\t\u00c2\3\2\2")
        buf.write("\2\13\u00c4\3\2\2\2\r\u00c6\3\2\2\2\17\u00c8\3\2\2\2\21")
        buf.write("\u00ca\3\2\2\2\23\u00cc\3\2\2\2\25\u00ce\3\2\2\2\27\u00d0")
        buf.write("\3\2\2\2\31\u00d2\3\2\2\2\33\u00d4\3\2\2\2\35\u00d6\3")
        buf.write("\2\2\2\37\u00d8\3\2\2\2!\u00da\3\2\2\2#\u00dc\3\2\2\2")
        buf.write("%\u00de\3\2\2\2\'\u00e0\3\2\2\2)\u00e2\3\2\2\2+\u00e4")
        buf.write("\3\2\2\2-\u00e6\3\2\2\2/\u00e8\3\2\2\2\61\u00ea\3\2\2")
        buf.write("\2\63\u00ec\3\2\2\2\65\u00ee\3\2\2\2\67\u00f0\3\2\2\2")
        buf.write("9\u00f2\3\2\2\2;\u00f5\3\2\2\2=\u00f9\3\2\2\2?\u00fd\3")
        buf.write("\2\2\2A\u0100\3\2\2\2C\u010a\3\2\2\2E\u0113\3\2\2\2G\u0116")
        buf.write("\3\2\2\2I\u011e\3\2\2\2K\u0123\3\2\2\2M\u0127\3\2\2\2")
        buf.write("O\u012c\3\2\2\2Q\u0133\3\2\2\2S\u013b\3\2\2\2U\u013f\3")
        buf.write("\2\2\2W\u0145\3\2\2\2Y\u014b\3\2\2\2[\u0154\3\2\2\2]\u0158")
        buf.write("\3\2\2\2_\u015f\3\2\2\2a\u0162\3\2\2\2c\u0165\3\2\2\2")
        buf.write("e\u016a\3\2\2\2g\u0171\3\2\2\2i\u0177\3\2\2\2k\u017d\3")
        buf.write("\2\2\2m\u0181\3\2\2\2o\u0186\3\2\2\2q\u018c\3\2\2\2s\u0191")
        buf.write("\3\2\2\2u\u0195\3\2\2\2w\u0199\3\2\2\2y\u019b\3\2\2\2")
        buf.write("{\u019d\3\2\2\2}\u019f\3\2\2\2\177\u01a1\3\2\2\2\u0081")
        buf.write("\u01a4\3\2\2\2\u0083\u01a6\3\2\2\2\u0085\u01a8\3\2\2\2")
        buf.write("\u0087\u01aa\3\2\2\2\u0089\u01ad\3\2\2\2\u008b\u01b0\3")
        buf.write("\2\2\2\u008d\u01b2\3\2\2\2\u008f\u01b4\3\2\2\2\u0091\u01b6")
        buf.write("\3\2\2\2\u0093\u01b8\3\2\2\2\u0095\u01ba\3\2\2\2\u0097")
        buf.write("\u01bc\3\2\2\2\u0099\u01bf\3\2\2\2\u009b\u01c1\3\2\2\2")
        buf.write("\u009d\u01c3\3\2\2\2\u009f\u01c5\3\2\2\2\u00a1\u01c9\3")
        buf.write("\2\2\2\u00a3\u01d7\3\2\2\2\u00a5\u01e2\3\2\2\2\u00a7\u01ee")
        buf.write("\3\2\2\2\u00a9\u01f4\3\2\2\2\u00ab\u01fb\3\2\2\2\u00ad")
        buf.write("\u0206\3\2\2\2\u00af\u020a\3\2\2\2\u00b1\u022b\3\2\2\2")
        buf.write("\u00b3\u022d\3\2\2\2\u00b5\u0236\3\2\2\2\u00b7\u0239\3")
        buf.write("\2\2\2\u00b9\u0244\3\2\2\2\u00bb\u00bc\5\u008fH\2\u00bc")
        buf.write("\u00bd\5\u0081A\2\u00bd\4\3\2\2\2\u00be\u00bf\t\2\2\2")
        buf.write("\u00bf\6\3\2\2\2\u00c0\u00c1\t\3\2\2\u00c1\b\3\2\2\2\u00c2")
        buf.write("\u00c3\t\4\2\2\u00c3\n\3\2\2\2\u00c4\u00c5\t\5\2\2\u00c5")
        buf.write("\f\3\2\2\2\u00c6\u00c7\t\6\2\2\u00c7\16\3\2\2\2\u00c8")
        buf.write("\u00c9\t\7\2\2\u00c9\20\3\2\2\2\u00ca\u00cb\t\b\2\2\u00cb")
        buf.write("\22\3\2\2\2\u00cc\u00cd\t\t\2\2\u00cd\24\3\2\2\2\u00ce")
        buf.write("\u00cf\t\n\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\t\13\2\2\u00d1")
        buf.write("\30\3\2\2\2\u00d2\u00d3\t\f\2\2\u00d3\32\3\2\2\2\u00d4")
        buf.write("\u00d5\t\r\2\2\u00d5\34\3\2\2\2\u00d6\u00d7\t\16\2\2\u00d7")
        buf.write("\36\3\2\2\2\u00d8\u00d9\t\17\2\2\u00d9 \3\2\2\2\u00da")
        buf.write("\u00db\t\20\2\2\u00db\"\3\2\2\2\u00dc\u00dd\t\21\2\2\u00dd")
        buf.write("$\3\2\2\2\u00de\u00df\t\22\2\2\u00df&\3\2\2\2\u00e0\u00e1")
        buf.write("\t\23\2\2\u00e1(\3\2\2\2\u00e2\u00e3\t\24\2\2\u00e3*\3")
        buf.write("\2\2\2\u00e4\u00e5\t\25\2\2\u00e5,\3\2\2\2\u00e6\u00e7")
        buf.write("\t\26\2\2\u00e7.\3\2\2\2\u00e8\u00e9\t\27\2\2\u00e9\60")
        buf.write("\3\2\2\2\u00ea\u00eb\t\30\2\2\u00eb\62\3\2\2\2\u00ec\u00ed")
        buf.write("\t\31\2\2\u00ed\64\3\2\2\2\u00ee\u00ef\t\32\2\2\u00ef")
        buf.write("\66\3\2\2\2\u00f0\u00f1\t\33\2\2\u00f18\3\2\2\2\u00f2")
        buf.write("\u00f3\5+\26\2\u00f3\u00f4\5!\21\2\u00f4:\3\2\2\2\u00f5")
        buf.write("\u00f6\5\5\3\2\u00f6\u00f7\5\13\6\2\u00f7\u00f8\5\13\6")
        buf.write("\2\u00f8<\3\2\2\2\u00f9\u00fa\5\35\17\2\u00fa\u00fb\5")
        buf.write("!\21\2\u00fb\u00fc\5\13\6\2\u00fc>\3\2\2\2\u00fd\u00fe")
        buf.write("\5!\21\2\u00fe\u00ff\5\'\24\2\u00ff@\3\2\2\2\u0100\u0101")
        buf.write("\5#\22\2\u0101\u0102\5\'\24\2\u0102\u0103\5!\21\2\u0103")
        buf.write("\u0104\5\t\5\2\u0104\u0105\5\r\7\2\u0105\u0106\5\13\6")
        buf.write("\2\u0106\u0107\5-\27\2\u0107\u0108\5\'\24\2\u0108\u0109")
        buf.write("\5\r\7\2\u0109B\3\2\2\2\u010a\u010b\5\17\b\2\u010b\u010c")
        buf.write("\5-\27\2\u010c\u010d\5\37\20\2\u010d\u010e\5\t\5\2\u010e")
        buf.write("\u010f\5+\26\2\u010f\u0110\5\25\13\2\u0110\u0111\5!\21")
        buf.write("\2\u0111\u0112\5\37\20\2\u0112D\3\2\2\2\u0113\u0114\5")
        buf.write("!\21\2\u0114\u0115\5\17\b\2\u0115F\3\2\2\2\u0116\u0117")
        buf.write("\5\25\13\2\u0117\u0118\5\37\20\2\u0118\u0119\5+\26\2\u0119")
        buf.write("\u011a\5\r\7\2\u011a\u011b\5\21\t\2\u011b\u011c\5\r\7")
        buf.write("\2\u011c\u011d\5\'\24\2\u011dH\3\2\2\2\u011e\u011f\5\'")
        buf.write("\24\2\u011f\u0120\5\r\7\2\u0120\u0121\5\5\3\2\u0121\u0122")
        buf.write("\5\33\16\2\u0122J\3\2\2\2\u0123\u0124\5\5\3\2\u0124\u0125")
        buf.write("\5\37\20\2\u0125\u0126\5\13\6\2\u0126L\3\2\2\2\u0127\u0128")
        buf.write("\5+\26\2\u0128\u0129\5\23\n\2\u0129\u012a\5\r\7\2\u012a")
        buf.write("\u012b\5\37\20\2\u012bN\3\2\2\2\u012c\u012d\5)\25\2\u012d")
        buf.write("\u012e\5+\26\2\u012e\u012f\5\'\24\2\u012f\u0130\5\25\13")
        buf.write("\2\u0130\u0131\5\37\20\2\u0131\u0132\5\21\t\2\u0132P\3")
        buf.write("\2\2\2\u0133\u0134\5\7\4\2\u0134\u0135\5!\21\2\u0135\u0136")
        buf.write("\5!\21\2\u0136\u0137\5\33\16\2\u0137\u0138\5\r\7\2\u0138")
        buf.write("\u0139\5\5\3\2\u0139\u013a\5\37\20\2\u013aR\3\2\2\2\u013b")
        buf.write("\u013c\5/\30\2\u013c\u013d\5\5\3\2\u013d\u013e\5\'\24")
        buf.write("\2\u013eT\3\2\2\2\u013f\u0140\5\5\3\2\u0140\u0141\5\'")
        buf.write("\24\2\u0141\u0142\5\'\24\2\u0142\u0143\5\5\3\2\u0143\u0144")
        buf.write("\5\65\33\2\u0144V\3\2\2\2\u0145\u0146\5\7\4\2\u0146\u0147")
        buf.write("\5\'\24\2\u0147\u0148\5\r\7\2\u0148\u0149\5\5\3\2\u0149")
        buf.write("\u014a\5\31\r\2\u014aX\3\2\2\2\u014b\u014c\5\t\5\2\u014c")
        buf.write("\u014d\5!\21\2\u014d\u014e\5\37\20\2\u014e\u014f\5+\26")
        buf.write("\2\u014f\u0150\5\25\13\2\u0150\u0151\5\37\20\2\u0151\u0152")
        buf.write("\5-\27\2\u0152\u0153\5\r\7\2\u0153Z\3\2\2\2\u0154\u0155")
        buf.write("\5\17\b\2\u0155\u0156\5!\21\2\u0156\u0157\5\'\24\2\u0157")
        buf.write("\\\3\2\2\2\u0158\u0159\5\13\6\2\u0159\u015a\5!\21\2\u015a")
        buf.write("\u015b\5\61\31\2\u015b\u015c\5\37\20\2\u015c\u015d\5+")
        buf.write("\26\2\u015d\u015e\5!\21\2\u015e^\3\2\2\2\u015f\u0160\5")
        buf.write("\13\6\2\u0160\u0161\5!\21\2\u0161`\3\2\2\2\u0162\u0163")
        buf.write("\5\25\13\2\u0163\u0164\5\17\b\2\u0164b\3\2\2\2\u0165\u0166")
        buf.write("\5\r\7\2\u0166\u0167\5\33\16\2\u0167\u0168\5)\25\2\u0168")
        buf.write("\u0169\5\r\7\2\u0169d\3\2\2\2\u016a\u016b\5\'\24\2\u016b")
        buf.write("\u016c\5\r\7\2\u016c\u016d\5+\26\2\u016d\u016e\5-\27\2")
        buf.write("\u016e\u016f\5\'\24\2\u016f\u0170\5\37\20\2\u0170f\3\2")
        buf.write("\2\2\u0171\u0172\5\61\31\2\u0172\u0173\5\23\n\2\u0173")
        buf.write("\u0174\5\25\13\2\u0174\u0175\5\33\16\2\u0175\u0176\5\r")
        buf.write("\7\2\u0176h\3\2\2\2\u0177\u0178\5\7\4\2\u0178\u0179\5")
        buf.write("\r\7\2\u0179\u017a\5\21\t\2\u017a\u017b\5\25\13\2\u017b")
        buf.write("\u017c\5\37\20\2\u017cj\3\2\2\2\u017d\u017e\5\r\7\2\u017e")
        buf.write("\u017f\5\37\20\2\u017f\u0180\5\13\6\2\u0180l\3\2\2\2\u0181")
        buf.write("\u0182\5+\26\2\u0182\u0183\5\'\24\2\u0183\u0184\5-\27")
        buf.write("\2\u0184\u0185\5\r\7\2\u0185n\3\2\2\2\u0186\u0187\5\17")
        buf.write("\b\2\u0187\u0188\5\5\3\2\u0188\u0189\5\33\16\2\u0189\u018a")
        buf.write("\5)\25\2\u018a\u018b\5\r\7\2\u018bp\3\2\2\2\u018c\u018d")
        buf.write("\5\61\31\2\u018d\u018e\5\25\13\2\u018e\u018f\5+\26\2\u018f")
        buf.write("\u0190\5\23\n\2\u0190r\3\2\2\2\u0191\u0192\5\37\20\2\u0192")
        buf.write("\u0193\5!\21\2\u0193\u0194\5+\26\2\u0194t\3\2\2\2\u0195")
        buf.write("\u0196\5\13\6\2\u0196\u0197\5\25\13\2\u0197\u0198\5/\30")
        buf.write("\2\u0198v\3\2\2\2\u0199\u019a\7-\2\2\u019ax\3\2\2\2\u019b")
        buf.write("\u019c\7/\2\2\u019cz\3\2\2\2\u019d\u019e\7,\2\2\u019e")
        buf.write("|\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0~\3\2\2\2\u01a1\u01a2")
        buf.write("\7>\2\2\u01a2\u01a3\7@\2\2\u01a3\u0080\3\2\2\2\u01a4\u01a5")
        buf.write("\7?\2\2\u01a5\u0082\3\2\2\2\u01a6\u01a7\7>\2\2\u01a7\u0084")
        buf.write("\3\2\2\2\u01a8\u01a9\7@\2\2\u01a9\u0086\3\2\2\2\u01aa")
        buf.write("\u01ab\7>\2\2\u01ab\u01ac\7?\2\2\u01ac\u0088\3\2\2\2\u01ad")
        buf.write("\u01ae\7@\2\2\u01ae\u01af\7?\2\2\u01af\u008a\3\2\2\2\u01b0")
        buf.write("\u01b1\7]\2\2\u01b1\u008c\3\2\2\2\u01b2\u01b3\7_\2\2\u01b3")
        buf.write("\u008e\3\2\2\2\u01b4\u01b5\7<\2\2\u01b5\u0090\3\2\2\2")
        buf.write("\u01b6\u01b7\7*\2\2\u01b7\u0092\3\2\2\2\u01b8\u01b9\7")
        buf.write("+\2\2\u01b9\u0094\3\2\2\2\u01ba\u01bb\7=\2\2\u01bb\u0096")
        buf.write("\3\2\2\2\u01bc\u01bd\7\60\2\2\u01bd\u01be\7\60\2\2\u01be")
        buf.write("\u0098\3\2\2\2\u01bf\u01c0\7.\2\2\u01c0\u009a\3\2\2\2")
        buf.write("\u01c1\u01c2\7}\2\2\u01c2\u009c\3\2\2\2\u01c3\u01c4\7")
        buf.write("\177\2\2\u01c4\u009e\3\2\2\2\u01c5\u01c6\t\34\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\bP\2\2\u01c8\u00a0\3\2\2\2")
        buf.write("\u01c9\u01ca\7*\2\2\u01ca\u01cb\7,\2\2\u01cb\u01cf\3\2")
        buf.write("\2\2\u01cc\u01ce\13\2\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0")
        buf.write("\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7,\2\2")
        buf.write("\u01d3\u01d4\7+\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\b")
        buf.write("Q\2\2\u01d6\u00a2\3\2\2\2\u01d7\u01db\7}\2\2\u01d8\u01da")
        buf.write("\13\2\2\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01de\3\2\2\2")
        buf.write("\u01dd\u01db\3\2\2\2\u01de\u01df\7\177\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e1\bR\2\2\u01e1\u00a4\3\2\2\2\u01e2")
        buf.write("\u01e3\7\61\2\2\u01e3\u01e4\7\61\2\2\u01e4\u01e8\3\2\2")
        buf.write("\2\u01e5\u01e7\n\35\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\bS\2\2")
        buf.write("\u01ec\u00a6\3\2\2\2\u01ed\u01ef\t\36\2\2\u01ee\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bT\2\2")
        buf.write("\u01f3\u00a8\3\2\2\2\u01f4\u01f8\t\37\2\2\u01f5\u01f7")
        buf.write("\t \2\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u00aa\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u0200\7$\2\2\u01fc\u01ff\n")
        buf.write("!\2\2\u01fd\u01ff\5\u00adW\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2")
        buf.write("\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0200\3")
        buf.write("\2\2\2\u0203\u0204\7$\2\2\u0204\u0205\bV\3\2\u0205\u00ac")
        buf.write("\3\2\2\2\u0206\u0207\7^\2\2\u0207\u0208\t\"\2\2\u0208")
        buf.write("\u00ae\3\2\2\2\u0209\u020b\4\62;\2\u020a\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3")
        buf.write("\2\2\2\u020d\u00b0\3\2\2\2\u020e\u0210\4\62;\2\u020f\u020e")
        buf.write("\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u020f\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u021f\3\2\2\2\u0213\u0215\7\60\2")
        buf.write("\2\u0214\u0216\4\62;\2\u0215\u0214\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u021b\5\u00b3Z\2\u021a\u0219\3\2")
        buf.write("\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u0213")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u0220\5\u00b3Z\2\u021f\u021c\3\2\2\2\u021f\u021e\3\2")
        buf.write("\2\2\u0220\u022c\3\2\2\2\u0221\u0222\4\62;\2\u0222\u0224")
        buf.write("\7\60\2\2\u0223\u0225\4\62;\2\u0224\u0223\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u022c\3\2\2\2\u0226\u0227\7\60\2")
        buf.write("\2\u0227\u0229\4\62;\2\u0228\u022a\5\u00b3Z\2\u0229\u0228")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022c\3\2\2\2\u022b")
        buf.write("\u020f\3\2\2\2\u022b\u0221\3\2\2\2\u022b\u0226\3\2\2\2")
        buf.write("\u022c\u00b2\3\2\2\2\u022d\u022f\t\6\2\2\u022e\u0230\t")
        buf.write("#\2\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232")
        buf.write("\3\2\2\2\u0231\u0233\4\62;\2\u0232\u0231\3\2\2\2\u0233")
        buf.write("\u0234\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\u00b4\3\2\2\2\u0236\u0237\13\2\2\2\u0237\u0238")
        buf.write("\b[\4\2\u0238\u00b6\3\2\2\2\u0239\u023f\7$\2\2\u023a\u023b")
        buf.write("\7^\2\2\u023b\u023e\t\"\2\2\u023c\u023e\n!\2\2\u023d\u023a")
        buf.write("\3\2\2\2\u023d\u023c\3\2\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0242\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0242\u0243\b\\\5\2\u0243\u00b8\3")
        buf.write("\2\2\2\u0244\u024c\7$\2\2\u0245\u0246\7^\2\2\u0246\u0249")
        buf.write("\t\"\2\2\u0247\u0249\n!\2\2\u0248\u0245\3\2\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024b\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3")
        buf.write("\2\2\2\u024d\u024f\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0250")
        buf.write("\7^\2\2\u0250\u0251\n\"\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u0253\b]\6\2\u0253\u00ba\3\2\2\2\31\2\u01cf\u01db\u01e8")
        buf.write("\u01f0\u01f8\u01fe\u0200\u020c\u0211\u0217\u021a\u021c")
        buf.write("\u021f\u0224\u0229\u022b\u022f\u0234\u023d\u023f\u0248")
        buf.write("\u024c\7\b\2\2\3V\2\3[\3\3\\\4\3]\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Assign = 1
    TO = 2
    ADD = 3
    MOD = 4
    OR = 5
    PROCEDURE = 6
    FUNCTION = 7
    OF = 8
    INTEGER = 9
    REAL = 10
    AND = 11
    THEN = 12
    STRING = 13
    BOOLEAN = 14
    VAR = 15
    ARRAY = 16
    BREAK = 17
    CONTINUE = 18
    FOR = 19
    DOWNTO = 20
    DO = 21
    IF = 22
    ELSE = 23
    RETURN = 24
    WHILE = 25
    BEGIN = 26
    END = 27
    TRUE = 28
    FALSE = 29
    WITH = 30
    NOT = 31
    DIV = 32
    PLUS = 33
    SUB = 34
    MUL = 35
    DI = 36
    NOTEQ = 37
    EQ = 38
    LESS = 39
    GREATER = 40
    LEQ = 41
    GEQ = 42
    LSB = 43
    RSB = 44
    COLON = 45
    LB = 46
    RB = 47
    SEMI = 48
    DDOT = 49
    COMMA = 50
    LK = 51
    RK = 52
    WS = 53
    Blockcomment1 = 54
    Blockcomment2 = 55
    Linecomment = 56
    Whitespace = 57
    IDENT = 58
    STRING_LITERAL = 59
    NUM_INT = 60
    NUM_REAL = 61
    ERROR_TOKEN = 62
    UNCLOSE_STR = 63
    ILLEGAL_ESP = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", "','", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "Assign", "TO", "ADD", "MOD", "OR", "PROCEDURE", "FUNCTION", 
            "OF", "INTEGER", "REAL", "AND", "THEN", "STRING", "BOOLEAN", 
            "VAR", "ARRAY", "BREAK", "CONTINUE", "FOR", "DOWNTO", "DO", 
            "IF", "ELSE", "RETURN", "WHILE", "BEGIN", "END", "TRUE", "FALSE", 
            "WITH", "NOT", "DIV", "PLUS", "SUB", "MUL", "DI", "NOTEQ", "EQ", 
            "LESS", "GREATER", "LEQ", "GEQ", "LSB", "RSB", "COLON", "LB", 
            "RB", "SEMI", "DDOT", "COMMA", "LK", "RK", "WS", "Blockcomment1", 
            "Blockcomment2", "Linecomment", "Whitespace", "IDENT", "STRING_LITERAL", 
            "NUM_INT", "NUM_REAL", "ERROR_TOKEN", "UNCLOSE_STR", "ILLEGAL_ESP" ]

    ruleNames = [ "Assign", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                  "U", "V", "W", "X", "Y", "Z", "TO", "ADD", "MOD", "OR", 
                  "PROCEDURE", "FUNCTION", "OF", "INTEGER", "REAL", "AND", 
                  "THEN", "STRING", "BOOLEAN", "VAR", "ARRAY", "BREAK", 
                  "CONTINUE", "FOR", "DOWNTO", "DO", "IF", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "TRUE", "FALSE", "WITH", "NOT", 
                  "DIV", "PLUS", "SUB", "MUL", "DI", "NOTEQ", "EQ", "LESS", 
                  "GREATER", "LEQ", "GEQ", "LSB", "RSB", "COLON", "LB", 
                  "RB", "SEMI", "DDOT", "COMMA", "LK", "RK", "WS", "Blockcomment1", 
                  "Blockcomment2", "Linecomment", "Whitespace", "IDENT", 
                  "STRING_LITERAL", "EscapeSequence", "NUM_INT", "NUM_REAL", 
                  "EXPONENT", "ERROR_TOKEN", "UNCLOSE_STR", "ILLEGAL_ESP" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[84] = self.STRING_LITERAL_action 
            actions[89] = self.ERROR_TOKEN_action 
            actions[90] = self.UNCLOSE_STR_action 
            actions[91] = self.ILLEGAL_ESP_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		s=self.text[1:-1]
            		self.text = s	
            	
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise ErrorToken(self.text)
            	
     

    def UNCLOSE_STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise IllegalEscape(self.text[1:])
            	
     


