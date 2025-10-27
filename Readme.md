Author: https://github.com/ninjamida

To use this mod for your Flashforge AD5X (it likely won't work with, and at any rate is useless for, the AD5M and AD5M Pro):

1. Install zMod: https://github.com/ghzserg/zmod
2. Run this command: ```ENABLE_PLUGIN name=nopoop```
3. Modify your slicer settings as described below

If these instructions do not make sense to you, please reconsider whether you want to use this highly experimental mod. It is best suited for those who already know their way around modding and customizing their 3D printers, and are willing to take some risks. With that being said, if you are not at that level yet but you really want to learn, there will always be people willing to offer help on various online forums - just be sure to explain very clearly what's going wrong or what part you're struggling to understand etc, and if relevant, try to provide screenshots / photos of your issue. The more information you can provide, the better people can help you.

Also - don't throw the poop bucket / chute away just yet. This eliminates poops DURING printing; it does not eliminate poops *before* a print (you'll get either one or three prior to a print, depending on whether a color change is needed), nor when loading colors through the menu while not printing.

If use_trash_on_print is set back to 1, behavior will be ALMOST like vanilla zMod, with two differences:
- Pause time when pooping after activating the fan is 4000ms, not 3000ms.
- When restoring the print head position after pooping, the print head first returns to the correct XY position, then only after that, returns to the Z position.

---

Overridden macros:

This mod overrides the following macros. If you have your own customizations to these, you will need to manually merge them with this mod's customizations. The versions currently present are based on the versions from zMod 1.6.1-146-g09bb977e.
  END_CHANGE_FILAMENT
  _IFS_REMOVE_PRUTOK
  _INSERT_PRUTOK_IFS
  _REZGEM_PRUTOK
  _SBROS_TRASH_DAVIM

---

Slicer settings:

In order to get the best results with this mod, some changes are needed to your slicer settings. I have written these settings based on Orca (not Orca-Flashforge); if you are using a different slicer, you will need to find the equivalent settings and values.

Printer settings:
  Multimaterial -> Purge in prime tower: Enable
  Multimaterial -> Filament load time: 21s (doesn't affect printing, just gives more accurate stats)
  Multimaterial -> Filament unload time: 27s (doesn't affect printing, just gives more accurate stats)

Filament settings:
  You do not need to change anything here. The "Multimaterial" settings will be ignored.

Print profile:
  Multimaterial -> Prime tower: Enable
  Multimaterial -> Prime tower: Extra flow for purging 200% (it seems that a higher flow when purging, means less actual purge volume is needed - presumably the faster flow helps pull residue out with it).
  Multimaterial -> Flush into objects' infill: Enable if you want (it will actually work now).
  Multimaterial -> Flush into objects' support: Enable if you want (it will actually work now).
  You might also want to increase the prime tower's brim (since the wipe tower will be taking a lot more punishment now, especially with PETG or mixed-material prints) and/or set the wall type to Rib

Flushing volumes:
  These are actually meaningful now! They will determine how much filament gets flushed into the wipe tower (or supports / infill if enabled).

---

Notes on materials

PLA: Works great.
PETG: Works fairly well. Wipe tower can be quite messy and look like it's going to fail, but (so far) I haven't had one actually fail. Blobbing can become an issue.
TPU: I've had mixed results - initially it refused to work, but then I altered some of the filament.json parameters (in particular the load speed) and have had a successful print involving TPU since.
ABS: Untested. Prediction: It will work almost as well as PLA.
Others: Untested, and I don't have enough experience with them to make predictions.

---

Notes on flush volumes

As a general note - using a value too low may result in color bleed (or worse, if it's a mixed-material rather than just mixed-color print). Using a value too high, on the other hand, only results in more waste and longer print times, but otherwise will not cause any problems. Therefore, if in doubt, it's better to err on the higher side. Even more so if the print is multi-color but single-material, and thus you can potentially use flush to supports / infill (it's generally not a great idea to use those in mixed-material prints).

Different colors of PLA: So far the majority of pairs seem to have ideal values in the range of 100 to 150. The sole exceptions I've found so far are white->black (90 is enough) and blue->white (150 is not enough).

PLA <-> PETG: Around 250 seems sufficient. Note that this was based on a single print where PETG was only used as support interfaces for a PLA print, where everything worked as expected (including no issues with layer adhesion).
PETG -> TPU 95A: Around 250 seems sufficient here too. This is also based on a single test print, but this print actually used both materials in the print itself.
TPU 95A -> PETG: On the other hand, 250 does not quite seem enough here - there were visible remnants of the TPU in some of the PETG parts afterwards.

All others: Untested. I suspect that 250ish will be sufficient for any material switch between two rigid filaments, or from a rigid filament to a flexible filament. I also suspect that color changes (same material) will be similar for other rigid filaments as they are for PLA, but probably need to be higher for flexible filaments.