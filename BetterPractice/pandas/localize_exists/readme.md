## Locate Elements in DataFrame

It is an answer to the question of

> I have two dataframes, df1 and df2, both have the same column date.
> The date column of df1 has about tens of millions of rows, and the date column of df1 is incomplete and may be duplicated. df2 is about a few thousand rows.
> The date column of df2 is complete and not repeated.
> How to use numpy vectorization to find out the date1 data that does not exist in df1 but exists in df2 and generate an numpy ndarray?
> I tried np.where and groupby.size, but I couldn't find the correct way to use them.
