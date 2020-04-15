package webClient;

import java.awt.image.BufferedImage;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

import javax.imageio.ImageIO;


public class webClient {
    // main function
	public static void main(String[] args) throws IOException {
		String buffer;
		Scanner scanner=new Scanner(System.in);
		String u1=scanner.nextLine();
		buffer = getWebContentByGet(u1, "UTF-8", 2000);
		System.out.println(buffer);
		String data = "2016024902/"+scanner.nextLine();
		String u2=scanner.nextLine();
		buffer = getWebContentByPost(u2, data, "UTF-8", 2000);
		System.out.println(buffer);
		String u3=scanner.nextLine();
		String s2=getWebContentByPost(u3, "2016024902", "UTF-8", 2000);
		System.out.println(s2);
	}
	
	// GET : send get message to web server through HTTP connection. When you send it, response would return.
	public static String getWebContentByGet(String urlString, final String charset, int timeout) throws IOException{
		if (urlString == null || urlString.length() == 0){
			return null;
		}
		urlString = (urlString.startsWith("http://")||urlString.startsWith("https://")) ? urlString
				: ("http://"+urlString).intern();
		URL url =new URL(urlString);
		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		conn.setRequestMethod("GET");
		conn.setRequestProperty("User-Agent",
				"2016024902/SERYOUNGYOON/WebClient/ComputerNetwork");
		conn.setRequestProperty("Accept", "text/html");
		conn.setConnectTimeout(timeout);
		try{
			if (conn.getResponseCode() != HttpURLConnection.HTTP_OK){
				return null;
			}
		}catch (IOException e){
			e.printStackTrace();
			return null;
		}
		InputStream input = conn.getInputStream();
		BufferedReader reader = new BufferedReader(new InputStreamReader(input,charset));
		String line = null;
		StringBuffer sb = new StringBuffer();
		while ((line = reader.readLine()) != null){
			sb.append(line).append("\r\n");
		}
		if (reader != null){
			reader.close();
		}
		if(conn != null){
			conn.disconnect();
		}
		return sb.toString();
		}
		
	// POST : send post message to web server through HTTP connection. When you send it, response would return.
	public static String getWebContentByPost(String urlString, String data, final String charset, int timeout) throws IOException{
		if (urlString == null || urlString.length() == 0){
			return null;
		}
		urlString = (urlString.startsWith("http://") || urlString.startsWith("https://")) ? urlString
				: ("http://" + urlString).intern();
		URL url = new URL(urlString);
		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		connection.setDoOutput(true);
		connection.setDoInput(true);
		connection.setRequestMethod("POST");
		connection.setUseCaches(false);
		connection.setInstanceFollowRedirects(true);
		connection.setRequestProperty("Content-Type", "text/html;charset=UTF-8");
		connection.setRequestProperty("User-Agent", "2016024902/SERYOUNGYOON/WebClient/ComputerNetwork");
		connection.setRequestProperty("Accept", "*/*");
		connection.setConnectTimeout(timeout);
		connection.connect();
		DataOutputStream out = new DataOutputStream(connection.getOutputStream());
		byte[] content = data.getBytes("UTF-8");
		out.write(content);
		out.flush();
		out.close();
		try {
			if (connection.getResponseCode() != HttpURLConnection.HTTP_OK)
				return null;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
		BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream(), charset));
		String line=null;
		StringBuffer sb = new StringBuffer();
		while ((line = reader.readLine()) != null) 
			sb.append(line).append("\r\n");
		if (reader != null) 
			reader.close();
		if (connection != null) 
			connection.disconnect();
		return sb.toString();
		}
}
