import java.util.*;
 
interface Expression {
	public void interpret(Stack<Integer> s);
}

class TerminalExpression_Number implements Expression {
	private int number;

	public TerminalExpression_Number(int number){
		this.number = number;
	}

	public void interpret(Stack<Integer> s){
		s.push(number);
	}
}

class TerminalExpression_Plus implements Expression {
	public void interpret(Stack<Integer> s){
		s.push(s.pop() + s.pop());
	}
}

class TerminalExpression_Minus implements Expression {
	public void interpret(Stack<Integer> s){
		int tmp = s.pop();
		s.push(s.pop() - tmp);
	}
}
 
class Parser {
	private ArrayList<Expression> parseTree = new ArrayList<Expression>(); // only one NonTerminal Expression here

	public Parser(String s) {
		for (String token : s.split(" ")) {
			if(token.equals("+")){
				parseTree.add( new TerminalExpression_Plus() );
			}
			else if(token.equals("-")){
				parseTree.add( new TerminalExpression_Minus() );
			}
			else{
				parseTree.add( new TerminalExpression_Number(Integer.valueOf(token)) );
			}
		}
	}

	public int evaluate() {
		Stack<Integer> context = new Stack<Integer>();

		for (Expression e : parseTree){
			e.interpret(context);
		}

		return context.pop();
	}
}

class interpreter {
	public static void main(String[] args) {
		System.out.println("'42 2 1 - +' equals " + new Parser("42 2 1 - +").evaluate());
	}
}