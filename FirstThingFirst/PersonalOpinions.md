## Personal Opinions

### Where to Put Useful Files

The **Onedrive** is great.

- Security
- Hands-off sync in good speed
- But, **5Gb is TOO SMALL**

You can put the **SMALL** files in there,
as they can be accessed easily when you are travelling around.

The other option is customized **SYNC** folder,
used for the dataset containing **BIG** or **TOO MANY** files.

- The files can be too large or too many
- The files can be saved in moveable disks
- The files can be private,
  if one does not want to share it
- The data is self-organized and self-explained,
  and it is naturally separated from the code using it.
- But, **there is NO VERSION CONTROL or AUTO SYNC for it**

### Better Practice of If Block

There are several kinds of writing styles of **If Block**.

```ps1
# Tight Version
if (Bool) {
  # One good job
} else {
  # Another good job
}

# Loose Version
if (Bool)
{
  # One good job
}
else
{
  # Another good job
}

# Better Version
# It shows where and how to switch, and where to stop
if (Bool) {
  # One good job
}
else {
  # Another good job
}
```

At the current stage, I prefer the **Better** version.
Since it shows where and how to switch, and where to stop **clearly**.

### My Coding Practice

The folder contains my coding manuscripts,
focus on the experience of how to code **quickly** and **efficiently**.

**Organization of Coding Project**

One should well organize the components, code and data, of the project,
in prior of coding anything.

A better suggestion is separating the data and code.

- The code can use the data by the API, so another data with the same format can be used.
- The data can be used by the other projects.
- The data can formulate its own dataset, in which it is easier to sync and transfer.

**Powerful Editor**

The first thing of an editor is its power of analysis the code.

- It should provide timely suggestions and basic auto-check functions.
- The structure visualization of the code is essentially important to understand and debug.

**Variables Naming**

The naming of the variables has been underestimated for a long time.
**I have not figured out how to do that properly.**

My current plan is,
taking 'my current opinion' for example

| Name           | Example            | Description                       |
| -------------- | ------------------ | --------------------------------- |
| Human Readable | my current opinion | Naming folder or file in OS       |
| Python         | my_current_opinion | Naming variable in python         |
| Python         | MyCurrentOpinion   | Naming class or package in python |
| JavaScript     | myCurrentOpinion   | Naming variable in JS             |
| HTML           | my-current-opinion | Naming id or class name in HTML   |
