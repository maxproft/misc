def sequence():
    global sim_info
    get_numbers_from_gui()
    save_vars_to_file("Monte Carlo Sequence")
    combinations = [[['z_dim',z_dim],['radius_1',radius_1],['radius_2',radius_2],['x_theta',x_theta]] for z_dim in [100,250,500] for radius_1 in [10,20] for radius_2 in [2.5,5,10] for x_theta in [10,20]]
    for frame_num in range(len(combinations)):
       sim_info = open(g.dictionary_SI['path_to_subfolder']+"simulation_infomation.txt","a")
       sim_info.write("\nFrame " + str(frame_num+1) + " of " + str(int(g.dictionary['s_step'])))
       sim_info.close()

       print( "\nmaking frame " + str(frame_num+1) + " of " + str(len(combinations)+1))
       title = g.dictionary_SI['title']
       for x in combinations[frame_num]:
            title+=' '+x[0]+'='+str(x[1])
            g.dictionary_SI['s_var']=x[0]
            change_units(x[1])
       Intensity = Average_Intensity(seqnum=str(frame_num+1))
       save(Intensity, "intensity"+str(frame_num+1))
       radial_intensity = radial(Intensity)
       save(radial_intensity, "radial_intensity"+str(frame_num+1))
       try:
           cumulative += np.asarray(Intensity)
       except NameError:
           cumulative = np.asarray(Intensity)
       if g.dictionary_SI['save_img'] == 1:
          Intensity_plot(Intensity, "intensity" + str(frame_num+1), title, 0)
          radial_intensity_plot(radial_intensity, "radial_intensity" + str(frame_num+1), title, 0)
       clear_mem()
    Intensity = cumulative / g.dictionary_SI['s_step']
    save(Intensity, "intensity")
    radial_intensity = radial(Intensity)
    save(radial_intensity, "radial_intensity")
    g.dictionary_SI['title'] = g.dictionary_SI['title']+" Averaged" + g.dictionary_SI['s_var']
    if g.dictionary_SI['save_img'] == 1:
      view_intensity()
    clear_mem()
    print( "Program Finished")

sequence()

