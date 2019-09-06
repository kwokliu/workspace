import java.io.* ;
import java.util.* ;
import java.lang.*;

public class PhoneDict
{
	public static void main( String [] argv ) throws IOException
	{
		Scanner src ;
		FileReader file = new FileReader( "words" );	//read words file
		src = new Scanner( file ) ;
		HashMap<String, String> d = new HashMap<String, String>() ;     
		
		while( src.hasNextLine() )
		{
			StringBuilder number = new StringBuilder();
			String words = src.nextLine();
			String word = words.toLowerCase();
			
			// get code number for each word
			for (int i = 0; i < word.length(); i++)
			{
				if (word.charAt(i) == 'a' || word.charAt(i) == 'b' || word.charAt(i) == 'c')
				{
					number.append(2);
				}
				else if (word.charAt(i) == 'd' || word.charAt(i) == 'e' || word.charAt(i) == 'f')
				{
					number.append(3);
				}
				else if (word.charAt(i) == 'g' || word.charAt(i) == 'h' || word.charAt(i) == 'i')
				{
					number.append(4);
				}
				else if (word.charAt(i) == 'j' || word.charAt(i) == 'k' || word.charAt(i) == 'l')
				{
					number.append(5);
				}
				else if (word.charAt(i) == 'm' || word.charAt(i) == 'n' || word.charAt(i) == 'o')
				{
					number.append(6);
				}
				else if (word.charAt(i) == 'p' || word.charAt(i) == 'q' || word.charAt(i) == 'r' || word.charAt(i) == 's')
				{
					number.append(7);
				}
				else if (word.charAt(i) == 't' || word.charAt(i) == 'u' || word.charAt(i) == 'v')
				{
					number.append(8);
				}
				else
				{
					number.append(9);
				}
				
				String key = number.toString();   
				d.put(words,key);  //Store keys and values into d map
			}
		}
		
		Set<String> keys = d.keySet() ;
		Scanner in = new Scanner (System.in); 	// read stdin
		while( in.hasNextLine() )
		{
			String testNum = in.nextLine();
			testNum = testNum.replaceFirst("^0*", "");   // remove leading 0
			testNum = testNum.replaceAll("0+","0");		// replace such as '000...' to '0'

			String[]  arrayNum = testNum.split("0");    //split by '0' and store the number into a array
			List<String> wordList = new ArrayList<String>();
			String l = "";
			for(int i=0;i<arrayNum.length;i++)
			{	
				String temp = "";
				if(d.containsValue(arrayNum[i]))  // if the map's keys has the match value
				{
					for( String s : keys )
					{
						if (d.get(s).equals(arrayNum[i]))
						{
							wordList.add(s);
							Collections.sort(wordList); //sort words
						}
					}
				
					if (wordList.size() > 1)		//if the number match at least two words
					{
						for ( int j = 0; j <wordList.size()-1; j++)
						{
							temp = temp+wordList.get(j)+"|";
						}
							l = l+"("+temp+wordList.get(wordList.size()-1)+") ";		
							wordList.clear();	//clear list
					}
					else			//the number match only one word
					{
						l = l + wordList.get(0)+" ";	
						
						wordList.clear();
					}
				}
				else		// no match word
				{
					int n = arrayNum[i].length();
						for (int k = 0; k < n; k++)
							{
								l = l + "*";	
							}
						l = l + " ";
				}
				
			}
			
			System.out.println(l);
        }		
	}
}