# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#identifier.
    def visitIdentifier(self, ctx:MPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MPParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varList.
    def visitVarList(self, ctx:MPParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MPParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:MPParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#formalParameterList.
    def visitFormalParameterList(self, ctx:MPParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listParam.
    def visitListParam(self, ctx:MPParser.ListParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#formalParameterSection.
    def visitFormalParameterSection(self, ctx:MPParser.FormalParameterSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parameterGroup.
    def visitParameterGroup(self, ctx:MPParser.ParameterGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#identifierList.
    def visitIdentifierList(self, ctx:MPParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitiveTypes.
    def visitPrimitiveTypes(self, ctx:MPParser.PrimitiveTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundTypes.
    def visitCompoundTypes(self, ctx:MPParser.CompoundTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#types.
    def visitTypes(self, ctx:MPParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statements.
    def visitStatements(self, ctx:MPParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileStatement.
    def visitWhileStatement(self, ctx:MPParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forStatement.
    def visitForStatement(self, ctx:MPParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifStatement.
    def visitIfStatement(self, ctx:MPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnStatement.
    def visitReturnStatement(self, ctx:MPParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callStatement.
    def visitCallStatement(self, ctx:MPParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MPParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withdoStatement.
    def visitWithdoStatement(self, ctx:MPParser.WithdoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continueandbreak.
    def visitContinueandbreak(self, ctx:MPParser.ContinueandbreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continueStatement.
    def visitContinueStatement(self, ctx:MPParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakStatement.
    def visitBreakStatement(self, ctx:MPParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#rightHandSides.
    def visitRightHandSides(self, ctx:MPParser.RightHandSidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#andthen.
    def visitAndthen(self, ctx:MPParser.AndthenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#orelse.
    def visitOrelse(self, ctx:MPParser.OrelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression1.
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#simpleExpression1.
    def visitSimpleExpression1(self, ctx:MPParser.SimpleExpression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#simpleExpression2.
    def visitSimpleExpression2(self, ctx:MPParser.SimpleExpression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#prefixExpression.
    def visitPrefixExpression(self, ctx:MPParser.PrefixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#relationalOperator.
    def visitRelationalOperator(self, ctx:MPParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#additiveoperator.
    def visitAdditiveoperator(self, ctx:MPParser.AdditiveoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#multiplicativeoperator.
    def visitMultiplicativeoperator(self, ctx:MPParser.MultiplicativeoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#factor.
    def visitFactor(self, ctx:MPParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#leftHandSides.
    def visitLeftHandSides(self, ctx:MPParser.LeftHandSidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#scalarVariable.
    def visitScalarVariable(self, ctx:MPParser.ScalarVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexExpression.
    def visitIndexExpression(self, ctx:MPParser.IndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexArray.
    def visitIndexArray(self, ctx:MPParser.IndexArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index.
    def visitIndex(self, ctx:MPParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexFunctionArray.
    def visitIndexFunctionArray(self, ctx:MPParser.IndexFunctionArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invocationExpression.
    def visitInvocationExpression(self, ctx:MPParser.InvocationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#functionCall.
    def visitFunctionCall(self, ctx:MPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#actualParameter.
    def visitActualParameter(self, ctx:MPParser.ActualParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literals.
    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unsignedInteger.
    def visitUnsignedInteger(self, ctx:MPParser.UnsignedIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unsignedReal.
    def visitUnsignedReal(self, ctx:MPParser.UnsignedRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#sign.
    def visitSign(self, ctx:MPParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boolean.
    def visitBoolean(self, ctx:MPParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#string.
    def visitString(self, ctx:MPParser.StringContext):
        return self.visitChildren(ctx)



del MPParser