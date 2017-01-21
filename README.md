# StackOverflow--Badge-Hunter
Read this to know [more about SO Badges](https://stackoverflow.com/help/badges)

###marshal.py


![Image of marshal](https://s28.postimg.org/b7btqx3yl/mar.png)

marshal.py script lists the url of questions in the terminal, that are likely to be of low quality   and also opens them in browser.
You can check these questions and flag them if they are really of low quality.

The logic behind this script is that, Newest Questions having large number of down votes are likely to be flagged.

This script eliminates the questions that are already flagged([on hold],[duplicate],[closed]).

Using this script daily, you can easliy find the questions to be flagged and earn the marshal flag faster.

This script opens the url in your default browser. It would be better to **use chrome**. You should be already logged in in your stackoverflow account there. This script doesnt include the login code.

You should have python3, BeautifulSoup installed in your system

####Flag Details
>You start with 10 flags per day.

>Based on your reputation and flagging history, you can end up with as many as 100 per day.

>Currently, that means you get an extra flag per day for every 2000 reputation points or 10 net helpful flags (helpful-declined).

>Since you  have an insane number of helpful flags, you're maxed out at 100 per day.

You can change the range of pages checked by modifying the code

![code marshal](https://s28.postimg.org/4i5aawiml/code.png)

Those numbers in range specifies the `page=` in url

Format of url : http://stackoverflow.com/questions?page=2&sort=newest



###copyeditor.py 


![Image of copy](https://s27.postimg.org/40of0ktsz/copy.png)

This python script lists questions with  spelling mistakes in thier title.

You can edit the titles of these questions.

This script uses enchant with us-english dictionary  and a file with technical terms(tech-terms.txt) that is usually identified as spelling mistakes.

The script list the urls of questions with spelling mistakes and the words that are identified as spelling mistakes in your terminal .
At present, some of these error words are technical terms like `iOS, onMouseOver  ` etc.
You can check through the output in the terminal and find the genuine english language spelling mistakes and then edit it by clicking their corresponding urls.

When you click a url from terminal, it opens  in your default browser. It would be better to **use chrome**. You should be already logged in in your stackoverflow account there. This script doesnt include the login code

terms.dict file contains some technical terms that may occur in question titles.It is used to avoid listing of technical terms as spelling mistakes.
But terms.dict is not complete. Feel free to add words.
###Guidelines to add words in terms.dict
1. Add news words to the file. Put each word in a new line

Then run the following commands in terminal

To avoid duplicate entries in the file

`awk '!seen[$0]++' terms.dict > output `

`cat output > terms.dict`

To sort words in alphabetical order

`sort terms.dict > output`

`cat output > terms.dict`

To make all words lowercase

`tr A-Z a-z < terms.dict > output`

`cat output > terms.dict `


Only titles are checked by the script now, we can extend it to check the content too.

If anybody is interested in the above, lets do it :+1

This script checks the questions that were active a long time ago.So that you can gain Archaeologist Badge too.

![Image of archeologist](https://s28.postimg.org/i117yws59/arc.png) 
![Image of excavator](https://s30.postimg.org/s3ocv8t41/excaa.png)

This is done by using the url that sorts the questions based on thier activeness

Format of url : http://stackoverflow.com/questions?page=84532&sort=active

We use pages like `82459, 78954 ` etc which will have questions that were active long time ago.

You can change the range of pages checked by modifying the code

####There are a handful of conditions where SO will stop accepting suggested edits:

>A large number of suggested edits by you were rejected in the past week (at least 5 more than one-third of your accepted edits).

>SO is out of empty slots in the queue 

>There is an edit to a particular post that was not approved yet.

>You are not logged in and the post is less than 10 minutes old.

>You have many suggested edits still in pending state.



![code arch](https://s29.postimg.org/s05sff26v/copycode.png)

Those numbers in range specifies the `page=` in url

You should have python3, BeautifulSoup,enchant installed in your system


###electorate.py 

![Image of elec](https://s24.postimg.org/e53nc6g79/elec.png)

This python script automates the process of voting.

You should give your login details for stackoverflow (email and password) in the script. 

If you use google or facebook login, this script cant help. If anybody is intrested we add that functionality too.

This script will vote on 30 questions (Provided you have 30 remaining votes that day).

You can run this script daily to get Electorate badge with ease.

As a side product, you will get following badges too.
![Image of copy](https://s24.postimg.org/tpb12pqbp/suff.png)

![Image of copy](https://s23.postimg.org/7w1wrkqff/ciciv.png)
![Image of supporter](https://s30.postimg.org/ngiath5r5/supp.png)
![Image of vox](https://s30.postimg.org/uv7mlurmp/vox.png)

For Vox populi, you can either modify the code to vote on 40 questions or manually vote on 10 more questions.

You will be voting on questions based on ther votes.

Format of url : https://stackoverflow.com/questions?page=1234&sort=votes

This script had made sure that you will vote only on questions having postive score (Check the code). So dont worry about voting in low quality posts. 

You should have python3, BeautifulSoup,selenium installed in your system




###These scripts may have lot of problems.
###Feel free to fork and give your corrections and improvements as Pull Requsets
###New badge hunters are also welcome


