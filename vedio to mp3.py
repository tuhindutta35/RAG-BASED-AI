#convert the vedios to mp3
import os
import subprocess

files=os.listdir("VEDIOS")

print(files)

for file in files:
    print(file)
    

    s =file 
    

    


# 1) Drop the domain part using the double-hyphen as the separator
    after_domain = s.split('--', 1)[-1]  # "CSS-Box-Model-Margin-Padding-Borders-Sigma_v720P"

# 2) Split by single hyphen and remove the last chunk ("Sigma_v720P")
    parts = after_domain.split('-')
    result = '-'.join(parts[:-1])

    print(result)  # CSS-Box-Model-Margin-Padding-Borders


# 1) Drop the domain part using the double-hyphen as the separator
    after_domain = s.split('--', 1)[-1]  # "CSS-Box-Model-Margin-Padding-Borders-Sigma_v720P"

# 2) Split by single hyphen and remove the last chunk ("Sigma_v720P")
    parts = after_domain.split('-')
    result = '-'.join(parts[:-1])

    print(result)  # CSS-Box-Model-Margin-Padding-Borders

    subprocess.run(['ffmpeg', '-i', f'VEDIOS/{file}',f"audios/{result}.mp3"])

  
   
    

  

