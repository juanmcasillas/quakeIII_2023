# Quake III 2023

How to setup Quake III in 2023, and use it on 4k HD screens with all the things. For convenience, I get all the required patches together and set the config, but you can set them manually

## <a name="fast_inst"></a>Fast installation.

1. A working version of Quake III. You should buy it, or use a downloadable version from internet. You need a valid CD key in order to work. This is the *recommended* method to go.

    - [Some random place in internet](https://steamunlocked.net/quake-3-arena-free-download/)
    - [Internet Archive](https://archive.org/details/quake-3-arena)

2. Get the latest zip in the [RELEASES](https://github.com/juanmcasillas/quakeIII_2023/releases/) section, and uncompress the files in the Quake3 installation. Then, go to the [Configuration](#configuration) section. The latest patches are included (Quake3e (08-04-2023 version), HQQ 3.7 and
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

## Server config

### Set the `server.cfg` file options

In order to start a dedicated server, we need to edit somethings in the `baseq3/server.cfg` file:

* `seta rconpassword "secret"      // sets RCON password for remote console`
* The game mode (`seta g_gametype 4`)
    - 0: deathmatch (free for all)
    - 1: one on one (tournament)
    - 2: not available in multiplayer
    - 3: team deathmatch
    - 4: capture the flag

By default, the server is configured as *deathmatch (FFA)*, with *10* minutes of timelimit and *100* frags max.

### Configure the launcher (`q3_server.bat`) arguments

Then, we need the *command line launcher* `q3_server.bat`

```bash
.\quake3e.ded.x64 +set dedicated 1 +set net_port 27969 +com_hunkMegs 1024 +exec server.cfg
```

* Start the server as `dedicated`, but *don't announce it in ID servers (2)*
* Set the net_port to `27969`
* Set the mem to 1 GB
* Run the config script

### Set the NAT in your router / firewall.

Just set a NAT rule from the PUBLIC ip the local IP of the computer running your quake3 server. In my case:

- `NAT port 27969/tcp to 192.168.100.203 27969/tcp`
- `NAT port 27969/udp to 192.168.100.203 27969/udp`

Then start the server.

* Server: `q3_server.bat`

### Test the configuration

1. Go to `Multiplayer` option menu
2. Set `Server: Local`
3. Click on `Specify`
4. Type the public ip or dns name in `Address:` field
5. Type the port (`27969`) in `Port:` field
6. Press `Fight` button

After you connect, you can go to menu pressing `ESC`, press `Server Info` and you can add the server to the *favorites* using `ADD TO FAVORITES` so next time, you only have to select `Server: Favorites` and click it.
