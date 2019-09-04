##
# outils de base
##

levels=("reveil" "tente" "sac_couchage" "sortir" "observation" "foret"
        "obs_foret" "ronces" "chemin" "clairiere" "cabane" "rentrer_cabane"
        "dodo" "matin" "decouverte_ruines" "ruines" "passage" "inscriptions"
        "train")

narrator=fnareoh
ncolors=$(tput colors 2>/dev/null)

if (( ncolors > 8 )); then
    bold="$(tput bold)"
    underline="$(tput smul)"
    standout="$(tput smso)"
    reset="$(tput sgr0)"
    black="$(tput setaf 0)"
    red="$(tput setaf 1)"
    green="$(tput setaf 2)"
    yellow="$(tput setaf 3)"
    blue="$(tput setaf 4)"
    magenta="$(tput setaf 5)"
    cyan="$(tput setaf 6)"
    white="$(tput setaf 7)"
fi

base_folder="$PWD"
bag=~/sac

nth () {
    local n="$1"
    shift $(( n + 1))
    echo "$1"
}

first () {
    nth 0 "$@"
}

expect_command () {
    [[ "$(first ${last_command})" == "$1" ]]
}

apply_colors () {
    local OLDIFS="$IFS"

    IFS=,
    for property in $1; do
         eval printf '%s' \$$property
    done

    IFS="$OLDIFS"
}

reset_colors () {
    printf '%s' "$reset"
}

disp () {
    apply_colors "$1"
    shift
    echo "$@"
    reset_colors
}

tell () {
    disp blue "<${narrator}>" "$@"
}

tell_me () {
    disp green '*' "$@" '*'
}

tell_ex () {
    disp red '/!\' "$@"
}

print_help_new_cmd () {
    echo
    echo "Aide mémoire :"
    tail -n 2 "${bag}/journal"
}

##
# exercices
##

##### level reveil #####

level_reveil_init () {
    tell "Hey. Hey ! Réveille-toi !"
    tell "Bien dormi ? Il faut reprendre la route,"
    tell "il reste encore beaucoup à découvir !"
    echo
    tell "Allez, debout !"
    echo
    tell_me "Ouch, dur le réveil. On est où déjà ?"
    tell_me "Oh parfait, mon journal ! Voyons voir..."

    cat "${bag}/journal"

    tell_ex "Utilise la commande 'pwd' de ton journal pour savoir où tu te trouves"

    mkdir -p "${base_folder}/tente"
    touch "${base_folder}/tente/sac_couchage"
    cat <<EOF > "${bag}/carte"
Chateau
   X---X        %%%
   |   |       %%%% Forêt
   X---X        %%%%

   Tente
      X
EOF
    cd "${base_folder}/tente"
}

level_reveil_check () {
    expect_command pwd
}

level_reveil_reward () {
    tell_me "Ah oui c'est vrai, la tente"
}

##### level tente #####

level_tente_init () {
    tell_ex "Affiche le contenu du dossier avec 'ls'"
    cat <<EOF >> "${bag}/journal"
    'ls' (qui vient de "LiSt")
        liste les fichiers et dossiers à ta position
EOF
    print_help_new_cmd
    tell_me "Une nouvelle commande ! Je vais la noter dans mon journal"
}

level_tente_check () {
    expect_command ls
}

##### level sac_couchage #####

level_sac_couchage_init() {
    tell_me "Récupère ton sac de couchage"
    tell_ex "Place le dans ton sac avec 'mv sac_couchage ~/sac/"
    cat <<EOF >> "${bag}/journal"
    'mv' (qui vient de "MoVe")
        déplace un fichier ou un dossier
EOF
    print_help_new_cmd
}

level_sac_couchage_check() {
    [[ -f "${bag}/sac_couchage" ]]
}

##### level sortir #####

level_sortir_init () {
    tell_me "Bon, il serait temps de sortir de cette tente quand même."
    tell_ex "Utilise 'cd ..' pour sortir du dossier"
    cat <<EOF >> "${bag}/journal"
    'cd forêt' (qui vient de "Change Directory")
        change de dossier
        par convention 'cd ..' permet de revenir en arrière dans les dossiers
EOF
    print_help_new_cmd
}

level_sortir_check () {
    [[ "$PWD" == "${base_folder}" ]]
}

level_sortir_reward () {
    mkdir -p "${base_folder}/forêt"
}

##### level observation #####

level_observation_init () {
    tell_ex "La commande 'tree' te permet d'avoir une vue d'ensemble des alentours"
    cat <<EOF >> "${bag}/journal"
    'tree'
        donne une vue d'ensemble de ta position
EOF
    print_help_new_cmd
}

level_observation_check () {
    expect_command tree
}

level_observation_reward () {
echo '
          |ZZzz                 ;;                           ::
    |Zzz  |     |Zzz       ; :: o :: ;                   :: `:;;`::
   /_\ /\ | /\ /_\        o::\ :| ::o/::               ` ::;;\`::\/
   |*|_||/_\||_|*|        :::o::o;::o:;                 :::\ ::::'"'"'`
   |.....|*|.....|     __  o :\:::/     ,;;,             :`::\://::
 __~| .. !~! .. |~___ (~ \____ | |_ ; :: o :: ;  _ __ _____| |__
 .*.|____|_|____|.*. ('"'"'    )   o::\ :| ::o/::     o)   ~~~~(     |^|
                      ~~~~~   /'"'"'    :::o::o;::o:;  `\  ~) ~  ~(  / ^ \
                                    o :\:::/:: ;       )~  o<  ~~(
                                        | |        )~~  ~   ~   ~~~(
                                             )~~    0< ~   0<   ~~(
'
}

##### level foret #####

level_foret_init () {
    tell "Regarde la forêt au loin !"
    tell "Ça a l'air joli, on y va ?"

    tell_ex "Déplace-toi dans la forêt"
}

level_foret_check () {
    [[ "$PWD" == "${base_folder}/forêt" ]]
}

level_foret_reward () {
    touch ronces
}

##### level obs_foret #####

level_obs_foret_init () {
    tell "Qu'est-ce que tu vois ?"
}

level_obs_foret_check () {
    expect_command ls
}

##### level ronces #####

level_ronces_init () {
    tell "Des ronces nous barrent la route !"
    tell "Il faut les enlever."

    tell_ex "Utilise 'rm ronces' pour les supprimer !"
    cat <<EOF >> "${bag}/journal"
    'rm ronces' (qui vient de "ReMove")
        supprime le fichier ronces
EOF
    print_help_new_cmd
}

level_ronces_check () {
    [[ ! -f "${base_folder}/forêt/ronces" ]]
}

level_ronces_reward () {
    mkdir chemin
}

##### level chemin #####

level_chemin_init () {
    tell "Regarde ! Un chemin est apparu."
    tell "Allons-y."
}

level_chemin_check () {
    [[ "$PWD" == "${base_folder}/forêt/chemin" ]]
}

level_chemin_reward () {
    mkdir clairière
}

##### level clairiere #####

level_clairiere_init () {
    tell "On n'est plus très loin, courage !"
}

level_clairiere_check () {
    [[ "$PWD" == "${base_folder}/forêt/chemin/clairière" ]]
}

##### level cabane #####

level_cabane_init () {
    tell "Il se fait tard..."
    tell "Construisons une cabane."
    tell_ex "'mkdir cabane' te permet de créer une cabane"
    cat <<EOF >> "${bag}/journal"
    'mkdir cabane' (qui vient de "MaKe DIRectory")
        créer le dossier cabane
EOF
    print_help_new_cmd
}

level_cabane_check () {
    [[ -d "${base_folder}/forêt/chemin/clairière/cabane" ]]
}

##### level rentrer_cabane #####

level_rentrer_cabane_init() {
    tell "Allons dormir dans la cabane."
}

level_rentrer_cabane_check() {
    [[ "$PWD" == "${base_folder}/forêt/chemin/clairière/cabane" ]]
}

##### level dodo #####

level_dodo_init () {
    tell_ex "Sors ton sac de couchage avec 'mv ~/sac/sac_couchage sac_couchage'"
}

level_dodo_check () {
    [[ -f "${base_folder}/forêt/chemin/clairière/cabane/sac_couchage" ]]
}

level_dodo_reward () {
    mv "${base_folder}/forêt/chemin/clairière/cabane/sac_couchage" "${bag}"
}

##### level matin #####

level_matin_init () {
    tell "Bien dormi ?"
    tell "Sortons de la cabane."
}

level_matin_check () {
    [[ "$PWD" == "${base_folder}/forêt/chemin/clairière" ]]
}

level_matin_reward () {
    mkdir "${base_folder}/forêt/chemin/clairière/ruines"
}

##### level decouverte_ruines #####

level_decouverte_ruines_init () {
    tell "Oh, des ruines au loin !"
}

level_decouverte_ruines_check () {
    [[ "$PWD" == "${base_folder}/forêt/chemin/clairière/ruines" ]]
}

level_decouverte_ruines_reward () {
    mkdir "${base_folder}/forêt/chemin/clairière/ruines/.passage_secret"
}

##### level ruines #####

level_ruines_init () {
    tell "Mais ! Il n'y a rien ici."
    tell "Comment continuer ?"
    tell_ex "'ls -a' te permet de voir les fichiers cachés."
    cat <<EOF >> "${bag}/journal"
    'ls -a'
        affiche tous les fichiers et dossiers, même ceux cachés
EOF
    print_help_new_cmd
}

level_ruines_check () {
    [[ "$PWD" == "${base_folder}/forêt/chemin/clairière/ruines/.passage_secret" ]]
}

level_ruines_reward () {
    touch "${base_folder}/forêt/chemin/clairière/ruines/.passage_secret/inscriptions"
}

##### level passage #####

level_passage_init () {
    tell "Un passage secret qui l'eut cru ?"
    tell "Regarde, sur le mur"
}

level_passage_check () {
    expect_command ls
}

##### level_inscriptions #####

level_inscriptions_init () {
    tell_ex "'cp inscriptions ~/sac/' pour copier les inscriptions dans ton sac"
    cat <<EOF >> "${bag}/journal"
    'cp inscriptions copie' (qui vient de "CoPy")
        copie un fichier dans un autre
EOF
    print_help_new_cmd
}

level_inscriptions_check () {
    [[ -f "${bag}/inscriptions" ]]
}

game_end () {
    echo Le jeu est terminé !
}

##### level_train #####

level_train_init () {
    tell "Il est temps de rentrer"
    tell_ex "Prend le train pour rentrer chez toi avec la commande 'sl'"
}

level_train_check () {
    expect_command sl
}

##
# logique de la boucle de jeu
##

current_level=0

level_init () {
    "level_${levels[$current_level]}_init" 2>/dev/null
}

level_check () {
    "level_${levels[$current_level]}_check"
}

level_reward () {
    "level_${levels[$current_level]}_reward"
}

try_enter_ex () {
    level_init
}

enter_ex () {
    if ! try_enter_ex; then
        game_end
        stop_game
        return 1
    fi
}

postexec () {
    if level_check $last_command; then
        echo
        echo
        level_reward 2>/dev/null || :
        current_level=$((current_level + 1))
        enter_ex
    fi
}

preexec () {
    if [ -n "$COMP_LINE" ] ||
       [ "$BASH_COMMAND" = "$PROMPT_COMMAND" ]; then
        return;
    fi

    last_command="$BASH_COMMAND"
}

setup_hooks () {
    PROMPT_COMMAND=postexec
    trap 'preexec' DEBUG
}

remove_hooks () {
    PROMPT_COMMAND=''
    trap ':' DEBUG
}

start_game () {
    mkdir -p -- "${base_folder}"
    mkdir -p -- "${bag}"
    cat <<EOF > "${bag}/journal"

    Journal d'aventure
    ~~~~~~~~~~~~~~~~~~

    Une héroïne du nom de $(echo "$USER" | tr . ' ')

    'cat ~/sac/journal'
        te permet d'afficher le contenu de ce journal
    'pwd' (qui vient de "Print Working Directory")
        affiche ta position dans tes dossiers
EOF

    cd "${base_folder}"
    enter_ex || return 1
    setup_hooks
}

stop_game () {
    remove_hooks
}

##
# UI
##

tp_linux () {
    start_game
}

aller_exo () {
    local old_level="${current_level}"
    current_level="$1"
    try_enter_ex || {
        echo "Il semblerait qu'il n'existe pas d'exo $1 !"
        current_level="${old_level}"
        return 1
    }

    echo "Exercice $1 sélectionné !"
    setup_hooks
}

sauter_exo () {
    aller_exo $((current_level + 1))
}
