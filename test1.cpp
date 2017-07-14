    #include <iostream>  
    #include <string.h>  
    #include <algorithm>  
    #include <stdio.h>  
      
    using namespace std;  
    const int N=250005;  
      
    struct State  
    {  
        State *pre,*go[26];  
        int step,v;  
        void clear()  
        {  
            v=0;  
            pre=0;  
            step=0;  
            memset(go,0,sizeof(go));  
        }  
    }*root,*last;  
      
    State statePool[N*2],*b[2*N],*cur;  
      
    void init()  
    {  
        cur=statePool;  
        root=last=cur++;  
        root->clear();  
    }  
      
    void Insert(int w)  
    {  
        State *p=last;  
        State *np=cur++;  
        np->clear();  
        np->step=p->step+1;  
        while(p&&!p->go[w])  
            p->go[w]=np,p=p->pre;  
        if(p==0)  
            np->pre=root;  
        else  
        {  
            State *q=p->go[w];  
            if(p->step+1==q->step)  
                np->pre=q;  
            else  
            {  
                State *nq=cur++;  
                nq->clear();  
                memcpy(nq->go,q->go,sizeof(q->go));  
                nq->step=p->step+1;  
                nq->pre=q->pre;  
                q->pre=nq;  
                np->pre=nq;  
                while(p&&p->go[w]==q)  
                    p->go[w]=nq, p=p->pre;  
            }  
        }  
        last=np;  
    }  
      
    char str[N];  
    int son[2*N][26];  
    char ch[2*N][26];  
    int cnt[2*N],c[2*N];  
      
    void Solve(int k)  
    {  
        int ct=0;  
        int now=0;  
        while(k)  
        {  
            for(int i=0; i<c[now]; i++)  
            {  
                State *tmp=statePool+son[now][i];  
                if(k>tmp->v)  
                    k-=tmp->v;  
                else  
                {  
                    str[ct++]=ch[now][i];  
                    now=son[now][i];  
                    k--;  
                    break;  
                }  
            }  
        }  
        str[ct]=0;  
        puts(str);  
    }  
      
    int main()  
    {  
        int n;  
        scanf("%s",str);  
        n=strlen(str);  
        init();  
        for(int i=0; i<n; i++)  
            Insert(str[i]-'a');  
        memset(cnt,0,sizeof(cnt));  
        memset(c,0,sizeof(c));  
        for(State *p=statePool; p!=cur; p++)  
            cnt[p->step]++;  
        for(int i=1; i<cur-statePool; i++)  
            cnt[i]+=cnt[i-1];  
        for(State *p=statePool; p!=cur; p++)  
            b[--cnt[p->step]]=p;  
        for(State *p=statePool; p!=cur; p++)  
            p->v=1;  
      
        int num=cur-statePool;  
        for(int i=num-1; i>=0; i--)  
        {  
            State *p=b[i];  
            for(int j=0; j<26; j++)  
            {  
                if(p->go[j])  
                {  
                    int x=p-statePool;  
                    int y=p->go[j]-statePool;  
                    son[x][c[x]]=y;  
                    ch[x][c[x]++]=j+'a';  
                    p->v+=p->go[j]->v;  
                }  
            }  
        }  
        int Q,k;  
        scanf("%d",&Q);  
        while(Q--)  
        {  
            scanf("%d",&k);  
            Solve(k);  
        }  
        return 0;  
    }  
