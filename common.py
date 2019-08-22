# The original source of all data is an excel workbook.
source_file = "data.xlsx"

# Those data are transformed into two data tables (dataframes)
data_file = "data.tsv"
meta_file = "meta.tsv"

# Color schemes for plots
import seaborn as sns
red_to_blue = sns.color_palette("RdBu", 10)
dark_palette = [red_to_blue[1], red_to_blue[8], ]
light_palette = [red_to_blue[3], red_to_blue[6], ]
reddish = red_to_blue[1]
bluish = red_to_blue[8]
