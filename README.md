# Quake III 2023

How to setup Quake III in 2023, and use it on 4k HD screens with all the things. For convenience, I get all the required patches together and set the config, but you can set them manually

## <a name="fast_inst"></a>Fast installation.

1. A working version of Quake III. You should buy it, or use a downloadable version from internet. You need a valid CD key in order to work. This is the *recommended* method to go.

    - [Some random place in internet](https://steamunlocked.net/quake-3-arena-free-download/)
    - [Internet Archive](https://archive.org/details/quake-3-arena)

2. Get the latest zip in the RELEASES section, and uncompress the files in the Quake3 installation. Then, go to the [Configuration](#configuration) section. The latest patches are included (Quake3e (08-04-2023 version), HQQ 3.7 and
Flexible HUD release 7)


## <a name="manual_inst"></a>Manual Installation

You can configure the required patches manually. Just download them and install in the required directories (`baseq3` and
`missionpack`). If you prefer a quick

1. A working version of Quake III. You should buy it, or use a downloadable version from internet. You need a valid CD key in order to work.
    - [Some random place in internet](https://steamunlocked.net/quake-3-arena-free-download/)
    - [Internet Archive](https://archive.org/details/quake-3-arena)

2. [Quake3e](https://github.com/ec-/Quake3e). This is a modern Quake III Arena engine aimed to be fast, secure and compatible with all existing Q3A mods. It is based on last non-SDL source dump of ioquake3 with latest upstream fixes applied. You can get the latest [Here](https://github.com/ec-/Quake3e/releases). Remember to get the zip that matches your architecture (e.g. `quake3e-windows-msvc-x86_64.zip`)

3. [High Quality Quake](https://www.moddb.com/mods/high-quality-quake). High resolution textures for menu, ingame HUD, 2D icons and all bugfixes from. The Unofficial Patch. Get the [latest](https://www.moddb.com/mods/high-quality-quake/downloads/hqq-v37) patch.

4. [Flexible HUD for IOQ3](https://clover.moe/flexible-hud-for-ioq3/). he default changes are that the HUD will be aspect correct and the Quake 3 start server menu will display 8 maps instead of 4. You can configure the HUD with cvars. Allows
to sit the HUD right in custom graphics configuration. Download the latest release (7) [from here](https://clover.moe/downloads/ztm-flexible-hud-r7.zip).


## <a name="configuration"></a>Configuration 

Ok, you have set all files using [Fast installation](#fast_inst) or [Manual Installation](#manual_inst), so lets go to configure it.

### Graphics customization

- edit `baseq3\autoexec.cfg` and change these vars to reflect your monitor settings
    * `seta r_customwidth "3840"  // witdh` 
    * `seta r_customheight "1600" // height` 
    * `seta r_customaspect "2.4"  // width / height (e.g. 3840 / 1600 = 2.4)`
    * `seta r_displayrefresh "144" // monitor freq`
    * `seta com_maxfps "144"       // match monitor freq`


- edit `baseq3\autoexec.cfg` and change this var to change your name:
    * `seta name "<YOUR_NAME>"`
    * `seta sv_hostname "<YOUR> server name" // for arena`


## Start the game.

* For Quake III standard edition: `q3.bat`
* For Quake III Arena: `q3_arena.bat`

