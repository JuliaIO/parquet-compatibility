# %%
import pyarrow as pa
import pyarrow.parquet as pq
import pathlib
import pandas as pd

p = pathlib.Path(__file__).parent.parent
#print(p)

Original_Data = p / "Original_Data"
Parquet_Files = p / "Parquet_Files"

compression_types = ["NONE", "SNAPPY", "GZIP", "ZSTD"]

csv_files = Original_Data.glob("*.csv")
for file in csv_files:
    dta = pd.read_csv(file, delimiter="|")
    for compression_type in compression_types:
        filename = (
            str(Parquet_Files.resolve())
            + "\\"
            + compression_type
            + "_pandas_pyarrow_"
            + str(file.stem)
            + ".parquet"
        )
        print(filename)
        dta.to_parquet(filename, compression=compression_type)
