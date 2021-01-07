package com.project_synthesis.items;

import com.project_synthesis.ProjectSynthesis;
import com.project_synthesis.init.ModItems;
import com.project_synthesis.util.IHasModel;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;

public class ItemBase extends Item implements IHasModel {

    public ItemBase(String name) {
        setUnlocalizedName(name);
        setRegistryName(name);
        setCreativeTab(CreativeTabs.MATERIALS);

        ModItems.ITEMS.add(this);
    }

    @Override
    public void registerModels() {
        ProjectSynthesis.proxy.registerItemRenderer(this, 0, "inventory");

    }
    
}
