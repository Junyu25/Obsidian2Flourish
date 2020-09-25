# Obsidian2Flourish
Convert Obsidian graph view to Flourish online preview
## Usage
I write a simple script to extract the network information from Obsidian,
So I can import them in to [Flourish](https://app.flourish.studio) and reproduce the interactive network graph in my website. 

`python ./Obsidian2Flourish.py Obsidian_Vault_Dir`

Then you will get tow `.csv` files in your current directory, They are:   
- `Links.csv`
- `Points.csv`

Simply import them into Network graph in [Flourish](https://app.flourish.studio), then you will get an interactive version that can embed on your website.   
PS: these file can also import to python and R, witch you can refer to [from Data to Viz](https://www.data-to-viz.com/#network).

## Demo:
Obsidian's Graph View:
![](img/demo_obsidian.png)

Interactive version in Flourish:
https://public.flourish.studio/visualisation/3581235/

