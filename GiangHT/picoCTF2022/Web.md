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

![image](https://user-images.githubusercontent.com/95273832/165497573-c6f9ed47-e2e8-4c47-90ca-02bb9de911d0.png)

![image](https://user-images.githubusercontent.com/95273832/165497353-093407af-4312-4a6a-8643-d82b156e5c3d.png)

Solution
I tried Username:admin & Password:admin123 =>login faile
After,i see source code in "login.php" , i have seen file "secure.js"
And i get  username === 'admin' && password === 'strongPassword098765'
=>login successful =>get Flag

![image](https://user-images.githubusercontent.com/95273832/165497518-73c026c7-f63f-4f4c-b7c8-536c335ad7be.png)

Flag:picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}

4)Search source

![image](https://user-images.githubusercontent.com/95273832/165497788-219a904a-f7a9-4da2-8907-d866fc60be37.png)

Solution
Now since the name of the question is search source then it pretty much directs us towards its source code. The source code in itself doesn’t have the flag but its files could surely do. But the problem is that we have several files to search which could be tiring and time consuming. A better approach is to give in to laziness and let the process be automated. For this we’ll make a copy of the entire website with the help of a tool called httrack as shown below.

![image](https://user-images.githubusercontent.com/95273832/165499061-7d855899-df0c-4949-bc5d-d06f938ce389.png)

The next step is to search every file for the flag for which we’ll use grep in a recursive manner. As we already know that the flag begins with pico we’ll leverage that and find the entire flag with the following command: grep -r picoCTF{

![image](https://user-images.githubusercontent.com/95273832/165499190-4cde7bef-58a3-4ab3-954a-cc521ed34b76.png)

Flag: picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}

5)Forbiddens path

![image](https://user-images.githubusercontent.com/95273832/165499287-8ec97f50-31b2-4487-a477-47d6403cc7c7.png)

Solution
This website has the useful feature of reading any file we want it too, given its path. With file paths, a preceeding ./ means the current directory, and ../ means the enclosing directory. Since we know that we are in /usr/share/nginx/html/, and want to access /flag.txt, we can just use the path ../../../../flag.txt to read the flag.

Flag:picoCTF{7h3_p47h_70_5ucc355_26b22ab3}

6)Power Cookie

![image](https://user-images.githubusercontent.com/95273832/165499410-9386908c-c16a-4ee7-bd4d-13ed09eea66b.png)

Solution
I used Cookie-editor in google chorme and edit cookie = 1 ,after reload website
=>get Flag

![image](https://user-images.githubusercontent.com/95273832/165499584-3d376dab-8f07-4117-a521-fcc30f868e70.png)

Flag:picoCTF{gr4d3_A_c00k13_0d351e23}

7)Roboto Sans

![image](https://user-images.githubusercontent.com/95273832/165499744-b459564c-c7ee-482f-b63b-a7f28da28bf3.png)

Solution
We are provided with a link to a webpage which doesn’t hold any useful information about the flag. However we do have a hint in the form of the question’s name. Lets see what the robot file has in store for us. We’ll add robots.txt after the URL of the website to visit it.
=>I received 1 code,From experience I realize it's base64 encoding decode it and get a plaintext,looks like path of URL.EXACTLY

![image](https://user-images.githubusercontent.com/95273832/165499860-5c817ac8-5766-4d0f-a237-dbdaba218e2e.png)

![image](https://user-images.githubusercontent.com/95273832/165500002-16debfcf-7627-4f5f-b5dd-a2068e831ac5.png)

![image](https://user-images.githubusercontent.com/95273832/165500172-151a4e60-4b1d-4d94-a009-d3660efde9ce.png)

Flag:picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}

8)Secrets

![image](https://user-images.githubusercontent.com/95273832/165500242-c6cd655b-c04e-4cf4-9ca4-7de20112d3c9.png)

Solution
When i read source code of website.i found folder "secret"

![image](https://user-images.githubusercontent.com/95273832/165500322-11932493-1d70-4802-bcb1-8c5461c2ddab.png)

after go to folder "secret".i continuous folder "hidden"

![image](https://user-images.githubusercontent.com/95273832/165500399-a129ba95-9860-452d-a3aa-502ca8d80135.png)

and coninue is folder superhidden =>get Flag

![image](https://user-images.githubusercontent.com/95273832/165500483-04654444-b227-4806-a4b2-acd05ee9c02a.png)

![image](https://user-images.githubusercontent.com/95273832/165500544-1805eb4a-2266-48f7-9df4-5d80f7f79451.png)

Flag:picoCTF{succ3ss_@h3n1c@10n_790d2615}

9)SQL Derect

![image](https://user-images.githubusercontent.com/95273832/165500622-ac7c1ecf-6f51-4d8b-b9d1-2482c3a88e99.png)

Solution
I run /dt to list the tables of the public scheme and i see a table flags
After i did 'select *' to take all data in table flags. Well done

![image](https://user-images.githubusercontent.com/95273832/165500806-169bea6f-f233-4069-a8d3-bb2c8f208251.png)

Flag:picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}

10)SQLiLite

![image](https://user-images.githubusercontent.com/95273832/165501080-64d43f7b-13e7-487b-af56-fae1a2d190f8.png)

Solution
I tried login using admin:admin and get following web page

![image](https://user-images.githubusercontent.com/95273832/165500987-ca44ef43-1db5-4a7c-90c2-b7b9859645e9.png)

I use SQL injection ' OR 1=1-- as a password, By using this SQL injection to check.

![image](https://user-images.githubusercontent.com/95273832/165501202-b0ec6798-ffef-4c54-a5e6-eef667f30e05.png)

Oh flag in source code

Flag:picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}




