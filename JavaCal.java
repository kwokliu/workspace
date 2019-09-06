// assignment3.java 
// CS265 Assignment3
// Parsing Infix Expressions
// 
// Author: Kwok Leung Liu  
//
// Date: 11/20/2016
//
// Version: 7 Update 101

import java.util.*;
import java.io.*;

/**
 * 
 * @author Kwok Leung Liu
 * 
 *  Class assisgnment3 parses infix expressions (described below) into appropriate Tokens
 *  (operator or operand), stored in some linear container (ArrayList ?), passes the infix
 *   expression to a function that returns the expression to postfix form, then passes it
 *    to a function which evaluates the postfix expression, returns an integer
 *
 */
public class assignment3 {
    
   
    	 /**
	 * This function transform string to infix expression
	 * @param stringArray input line
	 * @return list_tok<Token> postfix expression
	 * @throws Exception
	 */
	public static List<Token> infix2postfix(String[] stringArray) throws Exception {
            
            List<Token> in_fix = new LinkedList<>();
            List<Token> list_tok = new LinkedList<>();
            Stack postFixStack = new Stack();
            
            for (String element : stringArray) {
                if (element.matches("^-?\\d+$")) {
                    in_fix.add(new Operand(Integer.parseInt(element)));
                } else if (element.equals("+")) {
                    in_fix.add(new Operator(opType.ADD));
                } else if (element.equals("-")) {
                    in_fix.add(new Operator(opType.SUB));
                } else if (element.equals("*")) {
                    in_fix.add(new Operator(opType.MULT));
                } else if (element.equals("%")) {
                    in_fix.add(new Operator(opType.MOD));
                } else if (element.equals("/")) {
                    in_fix.add(new Operator(opType.DIV));
                } else if (element.equals("(")) {
                    in_fix.add(new Operator(opType.LPAR));
                } else if (element.equals(")")) {
                    in_fix.add(new Operator(opType.RPAR));
                }
            }
            
              
                 //Append a right paren ')' to the end of the input expression.
		in_fix.add(new Operator(opType.RPAR));    
                
                //Push a left paren '(' onto the stack.
		postFixStack.push(new Operator(opType.LPAR));
                
                //Start at the first token. For each token 
		while (!in_fix.isEmpty()){
			Token tok = in_fix.remove(0);
                        //If it is an operand, append it to the postfix expression.
			if (tok.isOperand())
				list_tok.add(tok);
			else if(tok.isOperator()){
				Operator op = (Operator) tok;
                                //If it is a left paren, push it onto the stack.
				if (op.getVal() == opType.LPAR )
					postFixStack.push(tok);
                                //If it is a right paren, pop operators from the stack and append to the postfix expression, until a left paren is encountered on the stack. Remove and discard the left paren.
				else if (op.getVal() == opType.RPAR){
                                      	Operator next_op = (Operator) postFixStack.pop();                                       
					while (next_op.getVal() != opType.LPAR ){
						list_tok.add((Token) next_op);
                                                next_op = (Operator) postFixStack.pop();
					}
				}
				else{
                                     //If it is an operator, then pop operators from the stack and append to the postfix expression while the operators
                                    //have equal or higher precedence than the current token. Push current token (operator) onto the stack. 
					if( Operator.compare((Operator)tok,(Operator)postFixStack.peek())>=0){
						list_tok.add((Token) postFixStack.pop());
					}
					postFixStack.push(tok);
				}				
                        }
		}
		return list_tok;
	}
        
        
	/**
	 * This function will take post fix expression and calculate the result
         * side effect: the function will print the Post fix and result
	 * @param post_fix expression
	 * @return int result of the calculation
	 * @throws Exception
	 */
	public static int evalPostfix(List<Token> post_fix ) throws Exception{
		Stack resultStack = new Stack();
		while(!post_fix.isEmpty()){
			Token tk = post_fix.remove(0);
 
			if(tk.isOperand()){
				Operand op = (Operand) tk;
				resultStack.push(op.getVal());
				System.out.print(op.getVal()+ " ");
			}
                        else if (tk.isOperator()){
				Operator op = (Operator) tk;
				int y = (int)resultStack.pop();
				int x = (int)resultStack.pop();
                            switch (op.getVal().getName()) {
                                case "Add":
                                    resultStack.push(x + y);
                                    System.out.print("+ ");
                                    break;
                                case "Sub":
                                    resultStack.push(x - y);
                                    System.out.print("- ");
                                    break;
                                case "Mult":
                                    resultStack.push(x * y);
                                    System.out.print("* ");
                                    break;
                                case "Div":
                                    resultStack.push(x / y);
                                    System.out.print("/ ");
                                    break;
                                case "Mod":
                                    resultStack.push(x % y);
                                    System.out.print("% ");
                                    break;
                            }
			}
		}
		return (int) resultStack.pop(); 
	}

        
        
        	 /**
	 * This function transform string to infix expression
	 * @param stringArray input line
	 * @return List<Token> infix expression
	 * @throws Exception
	 */
//	public static List<Token> string2infix(String[] stringArray) throws Exception {
//
//		List<Token> list_tok = new LinkedList<>();
//            for (String element : stringArray) {
//                if (element.matches("^-?\\d+$")) {
//                    list_tok.add(new Operand(Integer.parseInt(element)));
//                } else if (element.equals("+")) {
//                    list_tok.add(new Operator(opType.ADD));
//                } else if (element.equals("-")) {
//                    list_tok.add(new Operator(opType.SUB));
//                } else if (element.equals("*")) {
//                    list_tok.add(new Operator(opType.MULT));
//                } else if (element.equals("%")) {
//                    list_tok.add(new Operator(opType.MOD));
//                } else if (element.equals("/")) {
//                    list_tok.add(new Operator(opType.DIV));
//                } else if (element.equals("(")) {
//                    list_tok.add(new Operator(opType.LPAR));
//                } else if (element.equals(")")) {
//                    list_tok.add(new Operator(opType.RPAR));
//                }
//            }
//		return list_tok;
//	}
        
        
        
        
        
        /**
	 * This function transform infix expression to postfix expression
	 * @param in_fix expression
	 * @return postfix expression
	 * @throws Exception
	 */
//	public static List<Token> infix2postfix(List<Token> in_fix) throws Exception {
//		List<Token> list_tok = new LinkedList<>();
//                Stack postFixStack = new Stack();
//                
//                 //Append a right paren ')' to the end of the input expression.
//		in_fix.add(new Operator(opType.RPAR));    
//                
//                //Push a left paren '(' onto the stack.
//		postFixStack.push(new Operator(opType.LPAR));
//                
//                //Start at the first token. For each token 
//		while (!in_fix.isEmpty()){
//			Token tok = in_fix.remove(0);
//                        //If it is an operand, append it to the postfix expression.
//			if (tok.isOperand())
//				list_tok.add(tok);
//			else if(tok.isOperator()){
//				Operator op = (Operator) tok;
//                                //If it is a left paren, push it onto the stack.
//				if (op.getVal() == opType.LPAR )
//					postFixStack.push(tok);
//                                //If it is a right paren, pop operators from the stack and append to the postfix expression, until a left paren is encountered on the stack. Remove and discard the left paren.
//				else if (op.getVal() == opType.RPAR){
//                                      	Operator next_op = (Operator) postFixStack.pop();                                       
//					while (next_op.getVal() != opType.LPAR ){
//						list_tok.add((Token) next_op);
//                                                next_op = (Operator) postFixStack.pop();
//					}
//				}
//				else{
//                                     //If it is an operator, then pop operators from the stack and append to the postfix expression while the operators
//                                    //have equal or higher precedence than the current token. Push current token (operator) onto the stack. 
//					if( Operator.compare((Operator)tok,(Operator)postFixStack.peek())>=0){
//						list_tok.add((Token) postFixStack.pop());
//					}
//					postFixStack.push(tok);
//				}				
//                        }
//		}
//		return list_tok;
//	}
	
	/**
	 * Main method to get input from input.infix 
	 * Do the calculation and print postfix expression and result
	 * @param args
	 * @throws Exception
	 */
	public static void main(String args[]) throws Exception{
		// The name of the file to open.
        String fileName = "input.infix";
        try {
        	FileReader input_file= new FileReader(fileName);
        	BufferedReader input = new BufferedReader(input_file) ;
        	String line = input.readLine();
        	String[] split_line;
    		while (line!=null){
    			
    			split_line = line.split(" ");
//    			List<Token> infix = string2infix(split_line);
    			List<Token> postfix = infix2postfix(split_line);
    			int result = evalPostfix(postfix);
    			System.out.println( "= " + result);
    			line = input.readLine();
    		}
          } catch (FileNotFoundException e) {
           e.printStackTrace();
          } 	
	}
}
