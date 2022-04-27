1)Includes
![image](https://user-images.githubusercontent.com/95273832/165496507-1aea10b5-697b-4582-9272-4e740732e8b8.png)

Solution

hint:Is there more code than what the inspector initially shows?

So,I check code of website and open file "style.css" and "script.js".I get 2 path of flag
![image](https://user-images.githubusercontent.com/95273832/165496605-b771b3e3-c8b0-4502-ab27-893007da4ef0.png)
![image](https://user-images.githubusercontent.com/95273832/165496640-5128a469-c93d-405f-a243-2cb8ec31b2e4.png)

Flag:picoCTF{1nclu51v17y_1of2_f7w_2of2_b8f4b022}
2)Inspect HTML
![image](https://user-images.githubusercontent.com/95273832/165496814-6d9fcc38-1c96-4061-9fda-eac14d67ec4a.png)

Solution

As title,we just need check code of website 
![image](https://user-images.githubusercontent.com/95273832/165496928-70727dc3-a333-46ad-a32d-66d2be8ce289.png)

Flag:picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}

3)Local Authority

Solution

I tried Username:admin & Password:admin123 =>login faile
After,i see source code in "login.php" , i have seen file "secure.js"
And i get  username === 'admin' && password === 'strongPassword098765'
=>login successful =>get Flag

Flag:

4)

Solution
Now since the name of the question is search source then it pretty much directs us towards its source code. The source code in itself doesn’t have the flag but its files could surely do. But the problem is that we have several files to search which could be tiring and time consuming. A better approach is to give in to laziness and let the process be automated. For this we’ll make a copy of the entire website with the help of a tool called httrack as shown below.


The next step is to search every file for the flag for which we’ll use grep in a recursive manner. As we already know that the flag begins with pico we’ll leverage that and find the entire flag with the following command: grep -r pico


Flag: picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}

5)

Solution
This website has the useful feature of reading any file we want it too, given its path. With file paths, a preceeding ./ means the current directory, and ../ means the enclosing directory. Since we know that we are in /usr/share/nginx/html/, and want to access /flag.txt, we can just use the path ../../../../flag.txt to read the flag.

Flag:picoCTF{7h3_p47h_70_5ucc355_26b22ab3}

6)Power Cookie

Solution
I used Cookie-editor in google chorme and edit cookie = 1 
=>get Flag

Flag:picoCTF{gr4d3_A_c00k13_0d351e23}

7)Roboto Sans

Solution
We are provided with a link to a webpage which doesn’t hold any useful information about the flag. However we do have a hint in the form of the question’s name. Lets see what the robot file has in store for us. We’ll add robots.txt after the URL of the website to visit it.
=>I received 1 code,From experience I realize it's base64 encoding decode it and get a plaintext,looks like path of URL.EXACTLY

Flag:picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}

8)Secrets

Solution

When i read source code of website.i found folder "secret"
after go to folder "secret".i continuous folder "hidden"
and coninue is folder superhidden =>get Flag

Flag:picoCTF{succ3ss_@h3n1c@10n_790d2615}

9)SQL Derect

Solution

I run /dt to list the tables of the public scheme and i see a table flags

After i did 'select *' to take all data in table flags. Well done

Flag:picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}

10)SQLiLite

Solution

I tried login using admin:admin and get following web page

We can simply use SQL injection ' OR 1=1-- as a password, By using this SQL injection to check.

Oh flag in source code

Flag:picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}




