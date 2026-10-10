from Cond1Visitor import Cond1Visitor


class EvalVisitor1(Cond1Visitor):

    def visitProg(self, ctx):
        for s in ctx.stat():
            self.visit(s)

    def visitIfStat(self, ctx):
        condicion = self.visit(ctx.cond())
        if condicion:
            self.visit(ctx.stat(0))
        elif ctx.stat(1) is not None:
            self.visit(ctx.stat(1))

    def visitPrintStat(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)

    def visitCond(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.op.text == '<':
            return izq < der
        else:
            return izq > der

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        izq, der = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        return izq * der if ctx.op.text == '*' else izq / der

    def visitAddSub(self, ctx):
        izq, der = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        return izq + der if ctx.op.text == '+' else izq - der
