temp_s = """
			<div class="col-12 col-md-6">
						<div class="figure-holder mb-5" style="width: 100%; height: auto;">
							<img class="img-fluid" src="assets/images/v2/  """     
temp_e = """
" alt="image" style="width: 100%; height: auto;">
						</div><!--//figure-holder-->
					</div><!--//col-->
				"""

import os 

for root, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith(".jpg"):
            # print(file)
            print(temp_s + file + temp_e)
            
                