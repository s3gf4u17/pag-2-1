#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

void read_graph(std::string path) {
    std::fstream file(path,std::fstream::in);
    std::string buffer;
    std::map<int,std::vector<int>> graph;
    
    while(getline(file,buffer)) {
        if (buffer[0]=='#') continue;
        int n1 = std::stoi(buffer.substr(0,buffer.find('\t')));
        int n2 = std::stoi(buffer.substr(buffer.find('\t')+1,buffer.find('\t',1)));
        if (graph.find(n1)==graph.end()) {
            std::vector<int> init = {n2};
            graph.insert({n1,init});
        } else {
            graph[n1].push_back(n2);
        }
    }

    for (const auto &pair : graph) {
        std::cout << pair.first << ":";
        for (int i = 0 ;  i < pair.second.size() ; i++ ) std::cout << " " << pair.second[i];
        std::cout << "\n";
    }
}

int main() {
    read_graph("dane/Wiki-Vote.txt");
// print(find_cycle(g, 89))
    return 0;
}