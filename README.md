# Application Analysis

An analysis of Controls Applications using data such as execution count and lines of code.

## Data

All data is stored in the [app_data](./app_data.json) JSON file. This data was recoreded on October 6, 2023.

### Source of data

All data was sourced from the DBSRV database. For data that is based on a timespan, like `execution_count`, the timepsan was two years from the day data was taken.

### Overview of data

The data contains the following fields:

- `program`: The PA or SA number of an application, or the name of the user library
- `description`: Short description of application
- `type`: Type of application ('pas','sas', or 'uls')
- `status`: Active or obsolete
- `keeper`: Username of applicaiton keeper
- `backup`: Username of the backup to the keeper
- `author`: Username of original author
- `mod_on`: Timestamp of last modification
- `mod_by`: Username of who made the last modification
- `sqa_level`: Software Quality Assurance Level
- `execution_count`: The number of times an application was closed in the timespan the data was taken
- `index_page`: All index pages an application is mapped to
- `count`: Lines of code in CVS repository. This takes into account all `.h`, `.c`, `.cpp`, `.ftn`, and `.sql` files. In the case of user libraries `.proto` files were also taken into account.
