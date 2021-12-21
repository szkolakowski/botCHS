#include <bits/stdc++.h>
#include <string>
#include <fstream>
#include <iostream>
int main ()
{
    std::string c;
	system("git add -A");
	system("git rev-list HEAD --count > temp.txt");
	/// extract no. of commits
	std::ifstream ifs("temp.txt");
    std::string ret{ std::istreambuf_iterator<char>(ifs), std::istreambuf_iterator<char>() };
    ifs.close(); // must close the inout stream so the file can be cleaned up
    if (std::remove("temp.txt") != 0) {
        perror("Error deleting temporary file");
    }
    if (ret.size() == 0){
    	c = "0";
    }
    else{ /// last char is an enter (new line char) - need to remove it
    	for (int i=0; i < ret.size()-1; i++){
    		c += ret[i];
    	}
    }
    std::string a("git commit -m \"#");
	std::string b(" push [using script] \"");
	std::string str = a + c + b;
	const char *command = str.c_str();
	system(command);
	system("git push -u origin master");
	return 0;
}