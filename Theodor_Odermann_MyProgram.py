import Theodor_Odermann_Stats

def main():

		with open("500DayFruitData.txt", "r") as file:
			apple_set = []
			straw_set = []
			nana_set = []
			all_set = []
			
			for line in file:
				line = line.strip()
				if "apple" in line:
					new_line = line.split()
					apple_set.append(int(new_line[2]))
				elif "strawberry" in line:
					new_line = line.split()
					straw_set.append(int(new_line[2]))
				elif "banana" in line:
					new_line = line.split()
					nana_set.append(int(new_line[2]))
					
			all_set += apple_set
			all_set += straw_set
			all_set += nana_set
			
			apple_mean = Theodor_Odermann_Stats.Mean(apple_set)
			apple_median = Theodor_Odermann_Stats.Median(apple_set)
			
			
			straw_mean = Theodor_Odermann_Stats.Mean(straw_set)
			straw_median = Theodor_Odermann_Stats.Median(straw_set)
			
			nana_mean = Theodor_Odermann_Stats.Mean(nana_set)
			nana_median = Theodor_Odermann_Stats.Median(nana_set)
			
			all_mean = Theodor_Odermann_Stats.Mean(all_set)
			all_median = Theodor_Odermann_Stats.Median(all_set)
	
			with open("Theodor_Odermann_Output.txt", "w") as result_file:
				result_file.write(f"Apples Mean:{apple_mean: .2f}, Apples Median:{apple_median: .2f}\n")
				result_file.write(f"Bananas Mean:{nana_mean: .2f}, Bananas Median:{nana_median: .2f}\n")
				result_file.write(f"Strawberries Mean:{straw_mean: .2f}, Strawberries Median:{straw_median: .2f}\n")
				result_file.write(f"All Fruit Mean:{all_mean: .2f}, All Fruit Median:{all_median: .2f}\n")
				
			print(f"The mean number of apples eaten is {apple_mean: .2f}")
			print(f"The median number of apples eaten is {apple_median: .2f}")
			
			print(f"The mean number of bananas eaten is {nana_mean: .2f}")
			print(f"The median number of bananas eaten is {nana_median: .2f}")
			
			print(f"The mean number of strawberries eaten is {straw_mean: .2f}")
			print(f"The median number of strawberries eaten is {straw_median: .2f}")
			
			print(f"The mean number of all fruit eaten is {all_mean: .2f}")
			print(f"The median number of all fruit eaten is {all_median: .2f}")

if __name__ == "__main__":
	main()
