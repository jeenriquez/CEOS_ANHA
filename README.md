# ANHALIZE  (beta)

`ANHALIZE` is an analysis tool for the ANHA configuration of the NEMO model.

## Description

`ANHALIZE` is an analysis tool for the 
[Arctic and Northern Hemisphere Atlantic (ANHA)](https://canadian-nemo-ocean-modelling-forum-commuity-of-practice.readthedocs.io/en/latest/Institutions/UofA/Configurations/ANHA4/index.html) 
configuration of the [NEMO](https://www.nemo-ocean.eu/) model. The focus is on data manipulation, analysis, and visualization. 

This tool has been originally developed to support ocean modeling research at the 
Centre for Earth Observation Science (CEOS), at the University of Manitoba. 

NOTE: This code is stable, but new features are currently under development.


## Installation

Clone this [GitHub repo](https://github.com/PORTAL-CEOS/ANHALIZE): 

```
git clone https://github.com/PORTAL-CEOS/ANHALYZE.git
```

Install the dependencies in your [environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) with:

```
cd ANHALYZE/
python -m pip install -r requirements.txt
```

Then install the package with:

```
python -m pip install .
```


## Usage

Once installed you can import the library like this:

```
import anhalyze as ah
aa = ah.AnhaDataset(filename)
aaa = aa.sel(lat_range=[50,65],lon_range=[-93,-75])
```


### Example 

This  example requires an `ANHA` .nc file.

```
import anhalyze as ah

# Open file
aa = ah.AnhaDataset(filename)

# Do selection of lat_range, lon_range, and depth_range, in that order.
aaa = aa.sel([50,65],[-93,-75],[0,300])

# Plot region for a selected variable.
aaa.show_var_data_map(var='votemper')
``` 

## Additional Advanced Notes

### Masking

Masking is done internally. The default mask file will be automatically downloaded here `<package root path>/anhalyze/package_data/`,
the default mask name is `ANHA4_mask.nc`.

There are two more options for providing your own mask file:
 
#### Environment variable option:

You can add the following environmental variable(s) to your `.bash_profile` (or `.bashrc`, etc..), 
and edith paths to your needs:
``` 
#------------------------------------------------------------- 
#ANHALIZE setup
#-------------------------------------------------------------
export MASK_FILENAME='/root_path/user/../your_mask_location/mask_name.nc'
#-------------------------------------------------------------
```

#### Dynamic variable option:

You can provide your mask filename with full path when opening
an `ANHA*.nc` file, as follows:

```
import anhalyze as ah

# Open file
aa = ah.AnhaDataset(filename, mask_filename='mask_full_filename')
```

#### No-autodownload option:

If there is no mask available, `AnhaDataset` will attempt to download the default mask.
If you don't want this behaviour then edit the configuration file  `package_data.toml`,
located in `<package root path>/anhalyze/config/`. In the `[mask]` section, change
variable `autodownload_file` from 'true' to 'false'. This will prevent the file to be downloaded.
If you don't provide a valid mask alternative, the code will return an error message.

-----
## Version History

* 0.7 (planned)
    * To release `AnhalyzeLocation` class.
    * pip install functionality
* 0.6 (planned)
    * To release `AnhalyzeProject` class.
* 0.5 (upcoming)
    * First main release, includes:
      * `AnhaDataset` class
      * Basic functionality of single ANHA `nc` files. 
        * data reading/writing
        * region selection 
        * map plotting
    * See [commit change]() or See [release history]()
* 0.0.1
    * Current version in Beta. 

## License

This is a placeholder.



-------------------- Deprecated below this line. --------------------


Need to add the following environmental variables to your .bash_profile (or .bashrc, etc..), 
and edith paths to your needs:
``` 
#------------------------------------------------------------- 
#ANHALIZE setup
#-------------------------------------------------------------
export DATA_PATH='/root_path/user/NEMO/ANHA4/ANHA4-Wxx000-S/'
#-------------------------------------------------------------
```

