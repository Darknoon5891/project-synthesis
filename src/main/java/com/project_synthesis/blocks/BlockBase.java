package com.project_synthesis.blocks;

import com.project_synthesis.ProjectSynthesis;
import com.project_synthesis.init.ModBlocks;
import com.project_synthesis.init.ModItems;
import com.project_synthesis.util.IHasModel;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;

public class BlockBase extends Block implements IHasModel {

    public BlockBase(String name, Material material) {

        super(material);
        
        setUnlocalizedName(name);
        setRegistryName(name);
        setCreativeTab(CreativeTabs.MATERIALS);

        ModBlocks.BLOCKS.add(this);
        ModItems.ITEMS.add(new ItemBlock(this).setRegistryName(this.getRegistryName()));
    }

    @Override
    public void registerModels() {
        ProjectSynthesis.proxy.registerItemRenderer(Item.getItemFromBlock(this), 0, "inventory");
    }
    
}
