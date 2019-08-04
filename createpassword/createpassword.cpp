#include <iostream>

using namespace std;

int main()
{
    freopen("output.out","w",stdout);
    //for(int q=0;q<26;q++)
        for(int w=0;w<26;w++)
            for(int e=0;e<26;e++)
                for(int r=0;r<26;r++)
                    for(int t=0;t<26;t++)
                        for(int y=0;y<26;y++)
                            cout<<"BTQ"<<char(65+w)<<char(65+e)<<char(65+r)<<char(65+t)<<char(65+y)<<endl;
                        
}