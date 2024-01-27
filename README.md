# Yet Another Morse Code Converter

Hey. Yep, this is yet another morse code converter, aka **YAMCC**.

The main difference between this converter and other translators are, that this one actually provides full support for **Unicode Characters**!

## Encode mechanisms

YAMCC supports two encoding/decoding modes: *customize mode* and *takeover* mode.

### Customize mode

In customize mode, YAMCC simply encodes the input string into morse code, and then transforms
the encoded normal morse code (constructed with `.`, `-`) into user-defined code preset.

Specifically, for **unicode characters**, YAMCC first encodes them into unicode identifiers
(e.g. `\u0000`) and then adds an indicator character to notify the decoder that a unicode
character follows.

As for all identifiers (short code, long code, unicode splitter/ender, etc.) are all **totally
customizable** to the end user. If not specified, YAMCC will use a builtin preset (see `yamcc/__init__.py#L15`).

### Takeover mode

The base encode mechanism is the same as for takeover mode. However, takeover mode includes
a better preset of short/long code and unicode splitter/ender, etc. Specifically, the identifiers
are as follows:

- Short code: random member of `ascii_lowercase` upon each morse identifier.
- Long code: random member of `ascii_uppercase` upon each morse identifier.
- Morse segment separator: random member of `digits` upon each separator.
- Space: `+`.
- Unicode start identifier: `_`.
- Unicode end identifier: `$`.

If for some reason the encoder fails to encode a certain segment, it will fall back to `[ERROR]`
for that morse segment.

## Usage

Simply clone this repository and run the following command:

```bash
$ python -m yamcc
```

Then provide the required parameters and play around with it!

## Example

Example of using takeover mode to encode:

Input: `我现在的心态已经释怀了，毕竟有更重要的事等着我去做，何必苦苦在原地等待呢？`

Possible output: `_7bwY0Nzxtm7hhBAT4bXLKS3qMVDU9$1_7crU4OXzih0nfdCX6Deir8UVRVQ1$1_0nbR6lhcxx4OTimp6gnAFA4BJMmw4$0_1jaG1LYclh3Zyjgm8CDSpx8tsirG9$3_0ufZ0ykniu0cwOq2SqTs1uruIE8$3_0ywV8Iutfa1QPYST1PCBWS2rWJTO6$5_9mcZ2uskwr8Ccf3vtTb6zmRWS7$6_1xtG1ROxuv0m9PdZc3alDc8$7_7fiI8NWMQa1jITSQ9NaJl7wB6$4_0usU2Dqzmj7ZUNYW1TTNUD1DPZVB2$9_8kbR2uwzdJ6w6OKCpm5Wcazu9$9_8aiD3uuNy0vtTe7EJCQR9JzJh8$0_9opK5Vaecc7Mnqc4Xhx3clits0$1_1apD3YKgtp8vQ6Ece5txEg4$0_3okZ3Mtnby3EHpvr0PYSFE9EXCBw4$0_0ceO6Tufzx6Nbveu2frGf2xpynM1$5_8slC1BNCXu3kIEGE5GtGt4Gnp9$8_3ovC6VQSqm8EQGIi8SYQio5hCKOD4$5_1zrT7TMaqw3Zctqz7XJNtk2teqvR7$4_9viD6fenpQ9v7GRGin0Wcye0$8_9ilX2CRuwm0Mqbd0ndqtR4ITNIc0$1_3kaY9CBitm3JIbxg6rovrD8CGDFG4$8_9njG8Yggvn7aaYBA2sNXZV5kXJEA7$3_0ohQ5qjqja0bgzTG5Teyt0Gkoe9$7_1voD5lozus7UJSXA5neqoe3lV3$2_9kqA9mfYg8fnOr5AUQUT4RqSg7$5_0ofN3yoftU4rqNw2fzhcg5mgwam7$2_1tiA3yseif0pzKr6GtUo9qferj8$4_7cbO7ZCXzb1mxTWA0b9Xvcef3$0_2tjC5OLCbd8urQVE1u5Fpdrw5$2_2rqK7hlclk0NLwyw0yoMAD3KXGor3$9_4gpU0pxcaz1oqcJP8FVIGt6jaEd4$4_7cpK2sxmhh8QFrnm8ilwBG2OJFMJ2$8_2gnF3JUklo8Ybor2wgauW2EWHDt2$1_5agT5khvhm2dzLf1ABPgj4utywb7$3_5eeA3qvfcf1adoaQ7Csshx4mkFAQ6$2_6jfE0mjKv3wxRs1xYBSC7ccAk0$8`

## Drawbacks

From the example above, it is shown that the information density
of encoded YAMCC string is significantly low. It is not recommended
to use YAMCC for large string segments.

## Licensing

YAMCC is released under the MIT license. See the [LICENSE](LICENSE.md) file for more information.

## Contributing

YAMCC is a personal project and does not welcome contributing at
the moment.
