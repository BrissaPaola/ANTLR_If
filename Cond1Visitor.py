# Generated from Cond1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Cond1Parser import Cond1Parser
else:
    from Cond1Parser import Cond1Parser

# This class defines a complete generic visitor for a parse tree produced by Cond1Parser.

class Cond1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Cond1Parser#prog.
    def visitProg(self, ctx:Cond1Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#IfStat.
    def visitIfStat(self, ctx:Cond1Parser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#PrintStat.
    def visitPrintStat(self, ctx:Cond1Parser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#cond.
    def visitCond(self, ctx:Cond1Parser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#MulDiv.
    def visitMulDiv(self, ctx:Cond1Parser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#AddSub.
    def visitAddSub(self, ctx:Cond1Parser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#Parens.
    def visitParens(self, ctx:Cond1Parser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cond1Parser#Int.
    def visitInt(self, ctx:Cond1Parser.IntContext):
        return self.visitChildren(ctx)



del Cond1Parser