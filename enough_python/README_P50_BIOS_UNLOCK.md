
# 🔓 Lenovo P50 BIOS Unlock Guide (CH341A + Linux - Ubuntu)

This guide explains how to unlock or remove the **Supervisor Password** from a Lenovo ThinkPad P50 BIOS using:

- 🧰 CH341A USB programmer
- 🧪 SOIC8 test clip
- 🐧 Ubuntu Linux with `flashrom`

⚠️ **WARNING**: This is an advanced procedure. Do this only on your own machine. A wrong flash can brick your laptop. Always make a full backup.

---

## 🛠️ Requirements

### Hardware
- CH341A USB SPI programmer (Black Edition preferred)
- SOIC8 clip with Dupont cables
- 1.8V adapter (only if EEPROM is 1.8V — check chip marking)
- Laptop with Ubuntu
- Multimeter (optional but useful)
- Steady hands or soldering tools (only if clip fails)

### Software (on Ubuntu)
```bash
sudo apt update
sudo apt install flashrom xxd vim binwalk
```

---

## 🔍 Step 1: Identify Your BIOS Chip

1. Power off Lenovo P50.
2. Remove battery and AC adapter.
3. Unscrew and open the back cover.
4. Locate an 8-pin BIOS EEPROM chip. Example markings:
   - `W25Q128FV` or `MX25L128`
   - Manufacturer: Winbond, Macronix, etc.
5. Note the chip name for flashrom (optional).

---

## 🔌 Step 2: Connect the Programmer

1. Attach the **SOIC8 clip** to the chip with **pin 1** aligned (marked with a dot or notch).
2. Connect the other end to the **CH341A** using Dupont cables.
3. Plug CH341A into your Ubuntu laptop via USB.

---

## 💾 Step 3: Dump the Original BIOS

```bash
sudo flashrom -p ch341a_spi -r bios_backup.bin
cp bios_backup.bin bios_backup_original.bin
```

✅ Backup complete! You now have a full copy of your BIOS.

---

## ✂️ Step 4: Remove BIOS Password

### Option A: Using `vim` and `xxd` (Manual Method)
```bash
xxd bios_backup.bin | less
```

- Search for `"$SVS"` — the Supervisor Password block.
- Open with `vim`:
```bash
vim bios_backup.bin
:%!xxd
/search $SVS
```

- Replace the block with `00`s or match with a clean BIOS dump (32 bytes usually).
- Save:
```bash
:%!xxd -r
:w bios_unlocked.bin
```

---

## 🔁 Step 5: Flash the Modified BIOS

```bash
sudo flashrom -p ch341a_spi -w bios_unlocked.bin
```

✅ If no errors: flash was successful!

---

## 🔌 Step 6: Reassemble and Test

1. Unplug CH341A and SOIC8 clip.
2. Close the laptop casing and reinsert battery.
3. Power on and press `F1` to enter BIOS.
4. The Supervisor Password prompt should now be **gone**.

---

## 🧪 Optional: Compare Before and After

```bash
cmp bios_backup.bin bios_unlocked.bin
binwalk bios_unlocked.bin
```

---

## ✅ Summary

| Step | Command |
|------|---------|
| Install tools | `sudo apt install flashrom xxd vim` |
| Read BIOS | `sudo flashrom -p ch341a_spi -r bios_backup.bin` |
| Edit BIOS | `vim +:%!xxd bios_backup.bin` |
| Write BIOS | `sudo flashrom -p ch341a_spi -w bios_unlocked.bin` |
| Verify | `cmp`, `binwalk` |

---

## 📌 Notes

- If `flashrom` cannot detect your chip, double-check:
  - Clip alignment (pin 1)
  - USB port or power delivery
  - Voltage level (use 1.8V adapter if needed)

- Some chips may need to be desoldered if in-circuit reading fails.

- Always keep your `bios_backup_original.bin` safe.

---

## 🔐 Success

After rebooting, your Lenovo P50 should no longer ask for a Supervisor Password. You now have full access to BIOS configuration and can update/flash normally.
