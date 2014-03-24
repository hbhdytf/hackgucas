#########################################################################
# File Name: run.sh
# Author: sandy
# mail: sandy@luo.bo
# Created Time: 2014年03月23日 星期日 12时30分55秒
#########################################################################
#!/bin/bash
cd name
for files in $(echo *)
do
   ../hacker1.py ${files} &
done
echo "Finished"
