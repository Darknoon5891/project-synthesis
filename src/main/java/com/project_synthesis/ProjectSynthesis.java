package com.project_synthesis;

import com.project_synthesis.proxy.CommonProxy;
import com.project_synthesis.util.Refrences;

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.Mod.Instance;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;

@Mod(modid = Refrences.MODID, name= Refrences.NAME, version = Refrences.VERSION)
public class ProjectSynthesis {

    @Instance
    public static ProjectSynthesis Instance;

    @SidedProxy(clientSide = Refrences.CLIENT_PROXY_PATH, serverSide = Refrences.COMMON_PROXY_PATH)
    public static CommonProxy proxy;

    @EventHandler
    public void preInit(FMLPreInitializationEvent event) {}

    @EventHandler
    public void init(FMLInitializationEvent event) {
        System.out.println("Initialing");
    }

    @EventHandler
    public void postInit(FMLPostInitializationEvent event) {}
}