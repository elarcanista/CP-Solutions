#include <bits/stdc++.h>
using namespace std;

class LLNode{
public:
  int value;
  LLNode* next;
  LLNode* prev;

  LLNode(): value(-1), next(), prev(){}
  LLNode(int value):
    value(value), next(new LLNode()), prev(new LLNode()){}

  bool isLast(){
    return next->next == NULL;
  }

  bool isFirst(){
    return prev->prev == NULL;
  }
};

class LinkedList{
public:
  int size;
  LLNode* first;
  LLNode* last;

  LinkedList(): size(0), first(new LLNode()), last(new LLNode()){
    first->next = last;
    last->prev = first;
  }

  void addL(LLNode* curr, int v){
    LLNode* newN = new LLNode(v);
    curr->prev->next = newN;
    newN->prev = curr->prev;
    curr->prev = newN;
    newN->next = curr;
  }

  void addR(LLNode* curr, int v){
    LLNode* newN = new LLNode(v);
    curr->next->prev = newN;
    newN->next = curr->next;
    curr->next = newN;
    newN->prev = curr;
  }

  void remove(LLNode* curr){
    curr->prev->next = curr->next;
    curr->next->prev = curr->prev;
  }

  void remove(int v){
    LLNode* curr = first;
    while(curr->value != v)
      curr = curr->next;
    remove(curr);
  }
};

ostream &operator<<(ostream &os, const LinkedList &l){
  LLNode* curr = l.first->next;
  while(curr != l.last){
    os << curr->value << " ";
    curr = curr->next;
  }
  return os;
}
