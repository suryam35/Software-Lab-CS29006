#include<Windows.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<set>

using namespace std;

class Book
{
public :
    string title;
    string author;
    string release_date;
    string language;
    Book(string _title , string _author , string _release_date , string _language)
    {
        title = _title;
        author = _author;
        release_date = _release_date;
        language = _language;
    }
    ~Book() {}
};

class Novel : public Book
{
public:
    string type;
    vector<string> chap;
    map<string , string> chap_para;
    Novel(string _title , string _author , string _release_date , string _language) : Book(_title , _author , _release_date , _language)
    {
        type = "Novel";
    }
    ~Novel() {}
};

class Play : public Book
{
public:
    string type;
    vector<string> act;
    map<string , string> act_scene;
    map<string , string> scene_dia;
    Play(string _title , string _author , string _release_date , string _language) : Book(_title , _author , _release_date , _language)
    {
        type = "Play";
    }
    ~Play() {}
};

vector<string> files;
vector<pair<int , string>> chapter;
vector<pair<int , string>> paragraph;

void read_from_directory(char *path)
{
    WIN32_FIND_DATA file;
    char path1[] = "\\*.txt";
    strcat(path,path1);
    HANDLE search_handle=FindFirstFile(path,&file);
    if (search_handle)
    {
        do
        {
            string s;
            s = file.cFileName;
            files.push_back(s);
        }while(FindNextFile(search_handle,&file));
        FindClose(search_handle);

    }
}

string getTitleAndAuthor(string file_name)
{
    ifstream in;
    in.open(file_name);
    if(in.fail()) {
        cout << "No such file exists";
        in.close();
        return "";
    }
    string str;
    getline(in , str);
    while("Title" != str.substr(0 , 5))
        getline(in , str);
    string t = "";
    t += str;
    while("Author" != str.substr(0 , 6))
        getline(in , str);
    t += " " + str;
    in.close();
    return t;
}

void displayBook(string file_name)
{
    ifstream in;
    string str;
    in.open(file_name);
    if(in.fail()) {
        cout << "No such file exists";
        in.close();
        return;
    }
    getline(in , str);
    while("CHAPTER" != str.substr(0 , 7) && "SCENE" != str.substr(0 , 5))
        getline(in , str);
    while(1)
    {
        cout << "DO you want to display next 50 lines (y/n) : ";
        char c;
        cin >> c;
        if(c == 'n') break;
        int cnt = 1;
        while(in.eof() == 0 && cnt != 50)
        {
            cout << str << endl;
            cnt++;
            getline(in , str);
        }
        if(in.eof()) break;
    }
    in.close();
}

void searchTop(string bookname)
{
    chapter.clear();
    paragraph.clear();
    ifstream in;
    in.open(bookname);
    if(in.fail()) {
        cout << "No such file exists";
        in.close();
        return;
    }
    cout << "\nEnter the word to search for : ";
    string word;
    cin >> word;
    string str;
    getline(in , str);
    while("CHAPTER" != str.substr(0 , 7))
    {
        getline(in , str);
    }
    int chapter_num = 0 , para_num = 0;
    string chapt;
    while(in.eof() == 0)
    {
        //chapter_num++;
        para_num = 0;
        int total_count = 0;
        while(1)
        {
            string para = "";
            while(1)
            {
                if(str.substr(0 , 7) == "CHAPTER")
                {

                    int dot = str.find(".");
                    //chapter_num = stoi(str.substr(8 , dot-8));
                    //cout << str.substr(0 , 15) << " " << chapter_num << endl;
                    chapter_num++;
                    chapt = str;
                    getline(in , str);
                }
                //getline(in , str);
                para += str + " ";
                getline(in , str);
                if(str == "")
                {
                    para_num++;
                    int cnt = 0;
                    // count how many times the word occurs
                    char buffer[100000];
                    for(int i = 0 ; i < (int)para.size() ; i++)
                    {
                        buffer[i] = para[i];
                    }
                    buffer[(int)para.size()] = '\0';
                    char *token = strtok(buffer , " ");
                    char t[100000];
                    for(int i = 0 ; i < (int)word.size() ; i++)
                    {
                        t[i] = word[i];
                    }
                    t[(int)word.size()] = '\0';
                    while(token != NULL)
                    {
                        if(strcmp(t , token) == 0) cnt++;
                        token = strtok(NULL , " ");
                    }
                    paragraph.push_back({cnt , "PARA " + to_string(chapter_num) + "." + to_string(para_num) + " : " + para});
                    total_count += cnt;
                    break;
                }
            }
            getline(in , str);
            if(str == "")
            {
                // enter the total count
                chapter.push_back({total_count , chapt /*"CHAPTER " + to_string(chapter_num)*/});
                //if(in.eof()) break;
                break;
            }
        }
    }

    sort(chapter.begin() , chapter.end());
    sort(paragraph.begin() , paragraph.end());
    reverse(chapter.begin() , chapter.end());
    reverse(paragraph.begin() , paragraph.end());
    int k;
    cout << "Enter the value of k : ";
    cin >> k;
    cout << "\nThe top "<< k << " chapters are : \n";
    for(int i = 0 ; i < k ; i++)
    {
        cout << chapter[i].second << " : " << chapter[i].first << endl;
    }
    cout << "\nThe top " << k << " paragraphs are : \n";
    for(int i = 0 ; i < k ; i++)
    {
        cout << paragraph[i].second << " : " << paragraph[i].first << endl << endl;
    }
    in.close();
}

void getAllCharacters(string file, string character)
{
    transform(character.begin(), character.end(), character.begin(), ::toupper);
    ifstream in; // remeber to close it
    in.open(file);
    if(in.fail()) {
        cout << "No such file exists";
        in.close();
        return;
    }
    set<string> mainset;
    int ifcharfound = 0;
    int iffellowcharfound = 0;
    string a;
    getline(in, a);
    while("ACT" != a.substr(0,3))
    {
        getline(in ,a);
    }
    getline(in, a);
    int ispresent = 0;
    set<string> temp;
    while (1)
    {
        getline(in, a);

        if(in.eof() || a.substr(0,3)=="ACT" || a.substr(0,5)=="SCENE")
        {
            if(ispresent == 1)
            {
                for(auto x : temp)
                {
                    mainset.insert(x);
                }
                ispresent = 0;
            }
            if(in.eof())
                break;
            temp.clear();
            continue;
        }
        else
        {
            string s = a.substr(0,a.find("."));
            if(s == character){
                ispresent = 1;
                ifcharfound = 1;
            }
            if (std::all_of(s.begin(), s.end(), [](unsigned char c){ return std::isupper(c) || c == ' '; })) {
                if(s != character && s != "ALL" && s != "BOTH")
                    temp.insert(s);
            }
        }
    }
    if(!ifcharfound)
    {
        cout<<endl;
        cout<<"No character of this name is in the play"<<endl;
        cout<<endl;
        mainset.clear();
        in.close();
        return;
    }
    if(mainset.size() == 0)
    {
        cout<<endl;
        cout<<"No character appeared with this character in any scene"<<endl;
        cout<<endl;
        mainset.clear();
        in.close();
        return;
    }
    cout<<endl;
    cout<<"The names of character appeared with this character are"<<endl;
    for(auto x : mainset)
    {
        cout<<x<<endl;
    }
    cout<<endl;
    in.close();
    return;
}

int main(int argc , char *argv[])
{
    vector<Novel> novel;
    vector<Play> play;
    read_from_directory(argv[1]);      // reads from the directory to update the files
    ifstream in;
    in.open("index.txt");
    vector<string> index;        // index.txt   --->  filename.txt  title  author  type
    string str;
    while(in.eof() == 0)
    {
        getline(in , str);
        //string token = strtok(str , ' ');
        index.push_back(str);
    }
    vector<string> temp;
    for(string file_name : files)
    {
        if(file_name == "index.txt") continue;
        int flag = 1;
        for(string fn : index)
        {
            int t = fn.find(" ");
            string token = fn.substr(0 , t);
            if(file_name == token)
            {
                temp.push_back(fn);
                flag = 0;
                break;
            }
        }
        if(flag)
        {
            cout << "Enter the type of the book for "  << file_name << " : ";
            string type;
            cin >> type;
            string t = getTitleAndAuthor(file_name);
            temp.push_back(file_name + " " + t + " Type: " + type);
        }
    }
    in.close();
    ofstream out;
    out.open("index.txt");
    for(string file_name : temp)
    {
        out << file_name << endl;
    }
    out.close();

    int x;
    while(1)
    {
        cout << "\n********** MENU OPTIONS **********\n";
        cout << "1. List all books\n";
        cout << "2. Search for a book using author or title\n";
        cout << "3. Enter filename to display the book contents\n";
        cout << "4. Display top k chapters or paragraphs containing a given word in a book\n";
        cout << "5. Display scenes together to a given character\n";
        cout << "6. Exit the menu\n";
        cout << "\n Enter : ";
        cin >> x;
        if(x == 6) break;
        if(x == 1)
        {
            cout << "\n\n";
            in.open("index.txt");
            while(in.eof() == 0)
            {
                getline(in , str);
                if(str == "") continue;
                int ind = str.find("Type");
                cout << "File Name : " << str.substr(0 , ind) << endl;
            }
            in.close();
        }
        if(x == 2)
        {
            cout << "\nEnter the title or author : ";
            string t;
            cin >> t;
            transform(t.begin() , t.end() , t.begin() , ::tolower);
            in.open("index.txt");
            while(in.eof() == 0)
            {
                getline(in , str);
                if(str == "") continue;
                transform(str.begin() , str.end() , str.begin() , ::tolower);
                if(str.find(t) != -1)
                {
                    cout << str.substr(0 , str.find("Type")) << endl;
                }
            }
            in.close();
        }
        if(x == 3)
        {
            string name;
            cout << "\nEnter the file name : ";
            cin >> name;
            in.open("index.txt");
            int flag = 1;
            while(in.eof() == 0)
            {
                getline(in , str);
                if(str == "") continue;
                if(str.find(name) == -1) continue;
                else
                {
                    int ind = str.find("Title");
                    string file_name = str.substr(0 , ind-1);
                    displayBook(file_name);
                    flag = 0;
                    break;
                }
            }
            in.close();
            if(flag)
            {
                cout << "No book found with the given file name\n";
            }
        }
        if(x == 4)
        {
            cout << "Enter the filename of book (NOVEL) in which to search : ";
            string bookname;
            cin >> bookname;
            searchTop(bookname);
        }
        if(x == 5)
        {
            cout << "Enter the filename of book (PLAY) in which to search : ";
            string bookname;
            cin >> bookname;
            cout << "Enter the character to search for : ";
            string character;
            cin >> character;
            getAllCharacters(bookname , character);
        }
    }
}
